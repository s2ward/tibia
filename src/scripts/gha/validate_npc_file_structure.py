import os
import re
import sys

# Dictionary for characters to be replaced
replace_dict = {
    '\u2019': "'",
    '\u2018': "'",
    '\u2026': "...",
    '\u2013': "-",
    '\u00a0': " ",
    '\u201c': "\"",
    '\u201d': "\"",
    '\u00a7': "&",
    '\u00b4': "'"
}

# Function to check text files for errors
def check_txt_files_for_errors(folder):
    # Regular expressions for timestamp and number patterns
    timestamp_pattern = re.compile(r'^\d{2}:\d{2}(:\d{2})?', re.MULTILINE)
    number_pattern = re.compile(r'\[\d+\]')
    
    # Dictionaries to store file paths and their respective counts
    file_timestamp_counts = {}
    unwanted_char_counts = {}
    player_error_files = {}
    has_errors = False
    
    # Iterate through folder and subfolders
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Check only .txt files
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                try:
                    # Read file content
                    with open(filepath, "r", encoding='utf-8') as f:
                        lines = f.readlines()
                        content = ''.join(lines)
                except UnicodeDecodeError as e:
                    print(f"Error decoding file {filepath}: {e}")
                    has_errors = True
                    continue
                
                # Count occurrences of timestamp in content
                timestamp_lines = [i+1 for i, line in enumerate(lines) if timestamp_pattern.search(line)]
                # If timestamp found, add file path and count to dictionary
                if timestamp_lines:
                    file_timestamp_counts[filepath] = timestamp_lines
                    has_errors = True
                
                # Count occurrences of unwanted characters in content
                char_counts = {char: [i+1 for i, line in enumerate(lines) if char in line] for char in replace_dict}
                # Update unwanted character counts for the file
                for char, lines in char_counts.items():
                    if lines:
                        if filepath in unwanted_char_counts:
                            unwanted_char_counts[filepath][char] = lines
                        else:
                            unwanted_char_counts[filepath] = {char: lines}
                        has_errors = True

                # Check for "Player:" instances only if the content is not empty
                if content.strip() and "Player:" not in content:
                    player_error_files[filepath] = True
                    has_errors = True

    return file_timestamp_counts, unwanted_char_counts, player_error_files, has_errors

# Function to print a styled line break
def print_styled_line_break(character='-', length=25):
    print(character * length)

# Define path to folder containing text files
npc_folder_path = os.path.join("data/npcs/text")

# Check for errors in text files within the specified folder
result = check_txt_files_for_errors(npc_folder_path)

# Unpack the return values
file_timestamp_counts = result[0]
unwanted_char_counts = result[1]
player_error_files = result[2]
has_errors = result[3]

# Print errors related to "Player:" instances
if player_error_files:
    print("\nError - No 'Player:' instances found in the following files:")
    print_styled_line_break()
    for file_path in player_error_files.keys():
        print(f'  - {file_path}')
    print_styled_line_break()
    print(f'Total Files Missing "Player:": {len(player_error_files)}')
    print_styled_line_break()
# Print errors related to timestamps
if file_timestamp_counts:
    print("\nError - Timestamps found in the following files:")
    print_styled_line_break()
    for file_path, lines in file_timestamp_counts.items():
        print(f'  - {file_path}:')
        for line_number in lines:
            print(f'    - Line {line_number}')
        print_styled_line_break()
    print_styled_line_break()
    print(f'Total Files Timestamps Found: {len(file_timestamp_counts)}')
    print_styled_line_break()
# Print errors related to unwanted characters
if unwanted_char_counts:
    print("\nError - Unwanted characters found in the following files:")
    for file_path, char_lines in unwanted_char_counts.items():
        print_styled_line_break()
        print(f'  - {file_path}:')
        for char, lines in char_lines.items():
            print(f'    - "{char}":')
            for line_number in lines:
                print(f'        - Line {line_number}')
        print_styled_line_break()
    print(f'Total Files Unwanted characters Found: {len(unwanted_char_counts)}')
    print_styled_line_break()

# Print styled line break
print_styled_line_break()

# Exit with status 1 if any errors are found
if has_errors:
    sys.exit(1)
