import os
import json
import requests
from github import Github
from datetime import datetime, timezone

# update_project_status.py

def load_pr_data(pr_event_path):
    with open(pr_event_path, 'r') as f:
        return json.load(f)

def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d UTC")

def update_contributions_table(issue, pr_info, repo_name):
    timestamp = get_timestamp()
    existing_comment = next((comment for comment in issue.get_comments() if '### Contributions Table' in comment.body), None)
    existing_table = existing_comment.body.split('\n')[4:] if existing_comment else []
    new_entries = []

    # Dictionary to track the highest count for each contributor's file
    contributor_counts = {}

    # Parse the existing table to populate the contributor_counts dictionary
    for line in existing_table:
        parts = line.split('|')
        if len(parts) >= 6:
            try:
                opener = parts[1].strip()
                file_path = parts[2].strip().split('](')[-1].rstrip(')')
                count = int(parts[4].strip())
                contributor_counts[(opener, file_path)] = max(count, contributor_counts.get((opener, file_path), 0))
            except ValueError:
                continue  # Skip the header or any invalid lines

    for f in pr_info['files']:
        file_url = f'https://github.com/{repo_name}/blob/main/{f}'
        current_count = contributor_counts.get((pr_info["opener"], file_url), 0) + 1
        entry = f'| {pr_info["opener"]} | [{f}]({file_url}) | [{pr_info["title"]}]({pr_info["url"]}) | {current_count} | {timestamp} |'
        new_entries.append(entry)
        contributor_counts[(pr_info["opener"], file_url)] = current_count

    table = f'### Contributions Table\n\nLast updated: {timestamp}\n\n| Opener | Changed File | PR Link | Count | Timestamp |\n| --- | --- | --- | --- | --- |\n'
    table += '\n'.join(existing_table + new_entries).rstrip()

    if existing_comment:
        existing_comment.edit(table)
    else:
        issue.create_comment(table)

def prepare_discord_message(pr_info, npc_status, repo_name):
    content_lines = [
        f"**{pr_info['opener']}** has made a contribution! :first_place:",
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

    # Get relevant PR information
    pr_info = {
        'opener': pr.user.login,
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
