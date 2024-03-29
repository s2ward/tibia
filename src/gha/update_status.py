# src/update_status.py
import os
import json
import requests
from github import Github

# Read environment variables
token = os.environ.get('GITHUB_TOKEN')
issue_number = int(os.environ.get('ISSUE_NUMBER'))
repo_name = os.environ.get('GITHUB_REPOSITORY')
pr_event_path = os.environ.get('GITHUB_EVENT_PATH')
discord_webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')

# Load PR data
with open(pr_event_path, 'r') as f:
    pr_data = json.load(f)

# Initialize GitHub
g = Github(token)
repo = g.get_repo(repo_name)
issue = repo.get_issue(number=issue_number)
pr_number = pr_data['pull_request']['number']
pr = repo.get_pull(pr_number)
pr_opener = pr.user.login
pr_title = pr.title
pr_files = [f.filename for f in pr.get_files() if f.filename.startswith('npc/') and '_EMPTY.txt' not in f.filename]

if not pr_files:
    exit(0)

pr_url = pr.html_url
existing_comment = None

for comment in issue.get_comments():
    if '### Contributions Table' in comment.body:
        existing_comment = comment
        break

existing_table = existing_comment.body.split('\n')[4:] if existing_comment else []
new_entries = []

for f in pr_files:
    file_url = f'https://github.com/{repo_name}/blob/main/{f}'
    existing_contributions = [line for line in existing_table if f'| {pr_opener} |' in line]

    if existing_contributions:
        count = sum(1 for line in existing_contributions if f'| {pr_opener} |' in line) + 1
        updated_entry = f'| {pr_opener} | [{f}]({file_url}) | [{pr_title}]({pr_url}) | {count} |'
        existing_table.append(updated_entry)
    else:
        count = 1
        entry = f'| {pr_opener} | [{f}]({file_url}) | [{pr_title}]({pr_url}) | {count} |'
        new_entries.append(entry)

table = f'### Contributions Table\n\n| Opener | Changed File | PR Link | Count |\n| --- | --- | --- | --- |\n'
table += '\n'.join(existing_table + new_entries).rstrip()

if existing_comment:
    existing_comment.edit(table)
else:
    issue.create_comment(table)

# Send a message to the Discord channel
npc_status_output = os.environ.get('npc_status_output', 'No NPC status output found')

# Initialize content lines for Discord message
content_lines = [
    f"**{pr_opener}** has made a contribution! :first_place:",
    f"Issue: [{pr_title}](<{pr_url}>)",
]

# Collect file changes in a list
file_changes = []
for f in pr_files:
    # Enclose file_url and npsearch_url with < >
    file_url = f'https://github.com/{repo_name}/blob/main/{f}'
    npc_name = f.split('/')[-1].replace('.txt', '')
    npsearch_url = f'https://talesoftibia.com/npsearch?t={npc_name}'
    file_changes.append(
        f"File: [{f}](<{file_url}>) - Read on [NPSearch](<{npsearch_url}>)"
    )

# Once all file changes are collected
content_lines.append("\n**File Changes:**")
content_lines.extend(file_changes)

# Add project status at the end, ensuring any URL there is also enclosed in < >
npc_status_output = os.environ.get('npc_status_output', 'No NPC status output found')
content_lines.append("\n**Project Status**:\n" + (f"{npc_status_output}" if npc_status_output else "\n**Project Status**: *Data not available*"))

# Prepare the final Discord message content
discord_message_content = "\n".join(content_lines)

# Send a single message to the Discord channel
discord_message = {
    'content': discord_message_content
}
requests.post(discord_webhook_url, json=discord_message)
