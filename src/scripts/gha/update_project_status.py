import os
import json
import requests
import re
from github import Github
from datetime import datetime, timezone

# update_project_status.py

def load_pr_data(pr_event_path):
    with open(pr_event_path, 'r') as f:
        return json.load(f)

def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d UTC")

def extract_contributor(title):
    match = re.search(r'@(\w+)', title)
    return match.group(1) if match else None

def update_contributions_table(issue, pr_info, repo_name):
    timestamp = get_timestamp()
    existing_comment = next((comment for comment in issue.get_comments() if '### Contributions Table' in comment.body), None)
    if existing_comment:
        existing_table = existing_comment.body.split('\n')
    else:
        existing_table = []
    
    # Extract table content excluding headers
    table_lines = []
    header_encountered = False
    for line in existing_table:
        if line.startswith('| Opener | Changed File | PR Link | Count | Timestamp |'):
            header_encountered = True
        elif header_encountered and line.strip() and not line.startswith('| --- | --- | --- | --- | --- |'):
            table_lines.append(line)
    
    # Dictionary to track the highest count for each contributor
    contributor_counts = {}

    # Parse the existing table to populate the contributor_counts dictionary
    for line in table_lines:
        parts = line.split('|')
        if len(parts) >= 6:
            try:
                opener = parts[1].strip()
                count = int(parts[4].strip())
                contributor_counts[opener] = max(count, contributor_counts.get(opener, 0))
            except ValueError:
                continue  # Skip any invalid lines

    new_entries = []
    for f in pr_info['files']:
        file_url = f'https://github.com/{repo_name}/blob/main/{f}'
        current_count = contributor_counts.get(pr_info["contributor"], 0) + 1
        entry = f'| {pr_info["contributor"]} | [{f}]({file_url}) | [{pr_info["title"]}]({pr_info["url"]}) | {current_count} | {timestamp} |'
        new_entries.append(entry)
        contributor_counts[pr_info["contributor"]] = current_count

    table_header = f'### Contributions Table\n\nLast updated: {timestamp}\n\n| Opener | Changed File | PR Link | Count | Timestamp |\n| --- | --- | --- | --- | --- |\n'
    table_content = '\n'.join(table_lines + new_entries).rstrip()

    if existing_comment:
        existing_comment.edit(table_header + table_content)
    else:
        issue.create_comment(table_header + table_content)

def prepare_discord_message(pr_info, npc_status, repo_name):
    content_lines = [
        f"**{pr_info['contributor']}** has made a contribution! :first_place:",
        f"Issue: [{pr_info['title']}](<{pr_info['url']}>)",
        "\n**File Changes:**"
    ]

    for f in pr_info['files']:
        file_url = f'https://github.com/{repo_name}/blob/main/{f}'
        npc_name = f.split('/')[-1].replace('.txt', '')
        npsearch_url = f'https://talesoftibia.com/npsearch?t={npc_name}'
        content_lines.append(f"File: [{f}](<{file_url}>) - Read on [NPSearch](<{npsearch_url}>)")

    if npc_status:
        content_lines.extend([
            "\n**Project Status**:",
            f"Total NPCs: {npc_status['total_npcs']}",
            f"Verified: {npc_status['verified']['count']}/{npc_status['total_npcs']}, {npc_status['verified']['percentage']}%",
            f"Unverified: {npc_status['unverified']['count']}/{npc_status['total_npcs']}, {npc_status['unverified']['percentage']}%",
            f"Empty: {npc_status['empty']['count']}/{npc_status['total_npcs']}, {npc_status['empty']['percentage']}%",
            f"Unverified or Empty: {npc_status['unverified_or_empty']['count']}/{npc_status['total_npcs']}, {npc_status['unverified_or_empty']['percentage']}%"
        ])
    else:
        content_lines.append("\n**Project Status**: *Data not available*")

    return "\n".join(content_lines)

def send_discord_message(webhook_url, content):
    response = requests.post(webhook_url, json={'content': content})
    response.raise_for_status()

def load_npc_status(npc_status_json):
    if isinstance(npc_status_json, str):
        try:
            return json.loads(npc_status_json)
        except json.JSONDecodeError:
            print("Error decoding NPC status JSON. Using None instead.")
            return None
    elif isinstance(npc_status_json, dict):
        return npc_status_json
    else:
        print("Invalid NPC status data type. Using None instead.")
        return None

def main():
    # Load environment variables
    env = {
        'token': os.environ['GITHUB_TOKEN'],
        'issue_number': int(os.environ['ISSUE_NUMBER']),
        'repo_name': os.environ['GITHUB_REPOSITORY'],
        'pr_event_path': os.environ['GITHUB_EVENT_PATH'],
        'discord_webhook_url': os.environ['DISCORD_WEBHOOK_URL'],
        'npc_status_json': os.environ.get('NPC_STATUS_JSON')
    }

    # Initialize GitHub client
    g = Github(env['token'])
    repo = g.get_repo(env['repo_name'])
    issue = repo.get_issue(number=env['issue_number'])

    # Load PR data
    pr_data = load_pr_data(env['pr_event_path'])
    pr = repo.get_pull(pr_data['pull_request']['number'])

    # Extract contributor from title or use PR opener
    contributor = extract_contributor(pr.title) or pr.user.login

    # Get relevant PR information
    pr_info = {
        'contributor': contributor,
        'title': pr.title,
        'url': pr.html_url,
        'files': [f.filename for f in pr.get_files() if f.filename.startswith('data/npcs/text/') and '_EMPTY.txt' not in f.filename]
    }

    if not pr_info['files']:
        print("No relevant files changed. Exiting.")
        return

    # Update contributions table
    update_contributions_table(issue, pr_info, env['repo_name'])

    # Load NPC status
    npc_status = load_npc_status(env['npc_status_json'])

    # Prepare and send Discord message
    discord_message = prepare_discord_message(pr_info, npc_status, env['repo_name'])
    send_discord_message(env['discord_webhook_url'], discord_message)

if __name__ == "__main__":
    main()
