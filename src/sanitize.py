# USAGE
# python path/to/sanitize.py path/to/transcript.txt tibia_name
# Example usage:
# 
# python path/to/sanitize.py transcript.txt . Simula
# python path/to/sanitize.py path/to/transcript.txt Simula

import sys
import re
import os

# Dictionary of unicode characters to replace
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
    '\u00b4': "'",
    '\u00e9': "é",
    '\u00e0': "à",
    '\u00ed': "i",
}

def process_file(file_name, input_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # Count replacements and perform them
        counter = 0
        for key, value in replace_dict.items():
            if key in content:
                counter += content.count(key)
                content = content.replace(key, value)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Reopen the file for the original operations
        with open(file_path, 'r') as file:
            for line in file:
                line = re.sub(r'^\d{2}:\d{2}\s+', '', line)  # Remove timestamps
                line = re.sub(r'\[\d+\]', '', line)  # Remove [n] where n is any number
                line = re.sub(rf'({input_name})(\W)*:', 'Player:', line)  # Replace input_name with "Player" before the colon
                line = re.sub(rf'({input_name})(\W)+', 'Player ', line)  # Replace input_name followed by a non-word character with "Player"
                line = line.strip()  # Remove leading/trailing whitespaces

                if line:  # Print to console only if the line is not empty
                    print(line)

    print(f"Total characters replaced: {counter}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <input_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    input_name = sys.argv[2]
    process_file(file_name, input_name)
