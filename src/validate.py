import os
import re
import sys

replace_dict = {
    '\u2019': "'",
    '\u2018': "'",
    '\u2026': "...",
    '\u2013': "-",
    '\u00a0': " ",
    '\u201c': "\"",
    '\u201d': "\"",
    '\u00a7': "&",
    '\u00fc': "ü",
    '\u00b4': "'"
}

def check_txt_files_for_errors(folder):
    timestamp_pattern = re.compile(r'^\d{2}:\d{2}', re.MULTILINE)
    number_pattern = re.compile(r'\[\d+\]')
    
    has_errors = False
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError as e:
                    print(f"Error in file {filepath}: {e}")
                    has_errors = True
                    continue
                    
                player_count = content.count("Player:")

                if player_count == 0 and len(content.strip()) > 0:
                    print(f"Error: No 'Player:' instances found in file {filepath}")
                    has_errors = True

                if timestamp_pattern.search(content):
                    print(f"Error: Timestamp found in file {filepath}")
                    has_errors = True

                if number_pattern.search(content):
                    print(f"Error: Number pattern found in file {filepath}")
                    has_errors = True

                # Check for the unwanted characters
                for char in replace_dict:
                    if char in content:
                        print(f"Error: Found unwanted character '{char}' in file {filepath}")
                        has_errors = True

    return has_errors


folders = [os.path.join("..", "npc", folder) for folder in os.listdir(os.path.join("..", "npc")) if os.path.isdir(os.path.join("..", "npc", folder))]

print("Current working directory:", os.getcwd())

errors_found = False
for folder in folders:
    if check_txt_files_for_errors(folder):
        errors_found = True

if errors_found:
    sys.exit(1)
