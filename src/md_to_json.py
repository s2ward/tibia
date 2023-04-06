import os
import json

print("Current working directory:", os.getcwd())

def convert_md_to_json(folder):
    data = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                print(f"Opening file: {filepath}")
                with open(filepath, "r") as f:
                    lines = f.readlines()
                conversation = []
                for line in lines:
                    if line.strip():
                        speaker, text = line.strip().split(":", 1)
                        conversation.append({speaker.strip(): text.strip()})
                data.append({"file": filepath, "conversation": conversation})
    
    with open(os.path.join(folder, "..", "conversations.json"), "w") as f:
        json.dump(data, f)
        print(f"Writing output file to: {os.path.join(folder, '..', 'conversations.json')}")

folders = [os.path.join("..", "npc", folder) for folder in os.listdir(os.path.join("..", "npc")) if os.path.isdir(os.path.join("..", "npc", folder))]

for folder in folders:
    convert_md_to_json(folder)
