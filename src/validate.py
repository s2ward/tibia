import os
import json

print("Current working directory:", os.getcwd())

def check_txt_files_for_errors(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding='utf-8') as f:
                        lines = f.readlines()
                except UnicodeDecodeError as e:
                    print(f"Error in file {filepath}: {e}")
                    continue
                for i, line in enumerate(lines):
                    if line.strip() and ":" not in line:
                        print(f"Error in file {filepath} at line {i + 1}: {line.strip()}")
                        break


folders = [os.path.join("..", "npc", folder) for folder in os.listdir(os.path.join("..", "npc")) if os.path.isdir(os.path.join("..", "npc", folder))]

print("Current working directory:", os.getcwd())

for folder in folders:
    check_txt_files_for_errors(folder)
