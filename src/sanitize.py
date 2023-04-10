# USAGE
# python path/to/sanitize.py path/to/transcript.txt tibia_name
# Example usage:
# 
# python path/to/sanitize.py transcript.txt . Simula
# python path/to/sanitize.py path/to/transcript.txt Simula

import sys
import re
import os

def process_file(file_name, input_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r') as file:
        for line in file:
            line = re.sub(r'^\d{2}:\d{2}\s+', '', line)  # Remove timestamps
            line = re.sub(r'\[\d+\]', '', line)  # Remove [n] where n is any number
            line = re.sub(rf'({input_name})\s*:', 'Player:', line)  # Replace input_name with "Player" before the colon
            line = line.strip()  # Remove leading/trailing whitespaces
            
            # If line starts with input_name followed by a space, replace input_name with "Player"
            if line.startswith(input_name + ' '):
                line = 'Player' + line[len(input_name):]

            if line:  # Print to console only if the line is not empty
                print(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_name> <input_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    input_name = sys.argv[2]
    process_file(file_name, input_name)


# Bash instead of python: (not tested)

#!/bin/bash
#
#if [ "$#" -ne 2 ]; then
#    echo "Usage: $0 <file_name> <input_name>"
#    exit 1
#fi
#
#file_name="$1"
#input_name="$2"
#
#sed -e "s/^[0-9]\{2\}:[0-9]\{2\} //" \
#    -e "s/\[[0-9]\+\]//" \
#    -e "s/\(${input_name}\)\s*: /Player: /" \
#    -e "s/^${input_name}\s/Player /" "$file_name" | awk 'NF'
