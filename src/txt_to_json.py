import os
import json

def convert_txt_to_json(folder):
    data = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    lines = f.readlines()
                conversation = []
                for line in lines:
                    if line.strip():
                        speaker, text = line.strip().split(":", 1)
                        conversation.append({speaker.strip(): text.strip()})
                data.append({"file": filepath, "conversation": conversation})
    return data

folders = [os.path.join("..", "npc", folder) for folder in os.listdir(os.path.join("..", "npc")) if os.path.isdir(os.path.join("..", "npc", folder))]

all_data = []

for folder in folders:
    all_data.extend(convert_txt_to_json(folder))

# Remove extra newlines
for conv in all_data:
    for line in conv["conversation"]:
        speaker = list(line.keys())[0]
        line[speaker] = line[speaker].replace("\n\n", "\n")

with open(os.path.join("..", "api", "conversations.json"), "w") as f:
    json.dump(all_data, f)
