import os
import sys
import json
from pathlib import Path

def remove_status(mapping, file_path):
    """Remove the status for a given file path in the file mapping."""
    file_path = file_path.with_suffix('')
    parts = file_path.parts
    cur = mapping
    for part in parts[:-1]:
        cur = cur[part]
    if parts[-1] in cur:
        del cur[parts[-1]]
    else:
        print(f"Warning: Key '{parts[-1]}' not found in the mapping.")

def update_status(mapping, file_path, status):
    """Update the status for a given file path in the file mapping."""
    file_path = file_path.with_suffix('') 
    parts = file_path.parts
    cur = mapping
    for part in parts[:-1]:
        if part not in cur:
            cur[part] = {}
        cur = cur[part]
    cur[parts[-1]] = status

def get_status(base_dir, repo_dir, file_path):
    """Determine the status of a file based on its content."""
    base_file_path = base_dir / file_path.relative_to(repo_dir)

    if base_file_path.exists():
        with open(base_file_path) as f:
            base_content = f.read().strip()
    else:
        base_content = ""

    with open(file_path) as f:
        content = f.read().strip()

    if len(content) > len(base_content):
        return "VERIFIED"
    elif len(content) == 0:
        return "EMPTY"
    else:
        return "UNCHANGED"

def process_files(mapping, base_dir, repo_dir, files):
    """Process a list of files based on their status."""
    print(mapping)
    print(base_dir)
    print(repo_dir)
    print(files)
    for status, file_paths in files:
        if not file_paths:
            continue

        if status == "added":
            process_added_files(mapping, base_dir, repo_dir, file_paths)
        elif status == "modified":
            process_modified_files(mapping, base_dir, repo_dir, file_paths)
        elif status == "renamed":
            process_renamed_files(mapping, base_dir, repo_dir, file_paths)
        elif status == "deleted":
            process_deleted_files(mapping, base_dir, repo_dir, file_paths)

def process_added_files(mapping, base_dir, repo_dir, added_files):
    for added_file in added_files:
        file_path = repo_dir / added_file
        if file_path.is_file():
            status = get_status(base_dir, repo_dir, file_path)
            if status != "UNCHANGED":
                update_status(mapping, file_path.relative_to(repo_dir / 'npc'), status)

def process_modified_files(mapping, base_dir, repo_dir, modified_files):
    for modified_file in modified_files:
        file_path = repo_dir / modified_file
        if file_path.is_file():
            status = get_status(base_dir, repo_dir, file_path)
            if status != "UNCHANGED":
                update_status(mapping, file_path.relative_to(repo_dir / 'npc'), status)

def process_renamed_files(mapping, base_dir, repo_dir, renamed_files):
    for item in renamed_files:
        old_path, new_path = item
        old_path = Path(old_path).relative_to('npc')
        new_path = Path(new_path).relative_to('npc')
        remove_status(mapping, old_path)
        status = get_status(base_dir, repo_dir, repo_dir / 'npc' / new_path)
        update_status(mapping, new_path, status)

def process_deleted_files(mapping, base_dir, repo_dir, deleted_files):
    for deleted_file in deleted_files:
        file_path = repo_dir / deleted_file
        remove_status(mapping, file_path.relative_to(repo_dir / 'npc'))

if __name__ == '__main__':
    repo_dir = Path(sys.argv[1])
    base_dir = Path(sys.argv[2])

    file_statuses = ['added', 'modified', 'renamed', 'deleted']
    files = [(status, sys.argv[i+3].split('|')) for i, status in enumerate(file_statuses) if sys.argv[i+3]]

    print(f"repo_dir: {repo_dir}")
    print(f"base_dir: {base_dir}")
    print(f"files: {files}")

    with open(repo_dir / 'api' / 'file_mapping.json') as f:
        mapping = json.load(f)

    process_files(mapping, base_dir, repo_dir, files)

    with open(repo_dir / 'api' / 'file_mapping.json', 'w') as f:
        json.dump(mapping, f, indent=4)
