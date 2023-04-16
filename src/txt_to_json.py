import json
import os

# Recursively walks through npc/** 
# Extracts conversation data in its current form
# Creates single json db for use with NPSearch

def parse_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    conversation = []

    current_speaker = None
    prompt = None
    answers = []

    for line in lines:
        if line.strip():
            speaker, text = line.split(':', 1)
            text = text.strip()

            if speaker == 'Player':
                if current_speaker == speaker:
                    prompt += " " + text
                else:
                    if prompt is not None:  # Save the previous conversation if there is one
                        conversation.append({'prompt': prompt, 'answer': answers})
                    prompt = text
                    answers = []
            else:
                if current_speaker == speaker:
                    answers.append(text)
                else:
                    if answers:
                        answers[-1] += " " + text
                    else:
                        answers.append(text)

            current_speaker = speaker

    if prompt is not None:  # Save the last conversation
        conversation.append({'prompt': prompt, 'answer': answers})

    return conversation


def create_npc_data(file_path, name):
    conversation = parse_txt_file(file_path)

    npc_data = {
        'file': os.path.relpath(file_path),
        'name': name,
        'conversation': conversation
    }

    return npc_data


def save_to_json(npc_data_list, output_file):
    with open(output_file, 'w') as file:
        json.dump(npc_data_list, file, indent=4)

def process_files(input_dir, output_dir):
    npc_data_list = []

    for root, dirs, files in os.walk(input_dir):
        print(f"Current directory: {root}")  # Debugging: print the current directory being processed
        print(f"Files in directory: {files}")  # Debugging: print the files in the current directory

        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")  # Debugging: print the file being processed

                # Extract NPC name from the file name without underscore and file extension
                npc_name = os.path.splitext(file)[0].replace('_', ' ')

                npc_data = create_npc_data(file_path, npc_name)
                npc_data_list.append(npc_data)

    print(f"Total NPCs processed: {len(npc_data_list)}")  # Debugging: print the total number of NPCs processed

    output_file = os.path.join(output_dir, 'conversations.json')
    save_to_json(npc_data_list, output_file)

if __name__ == '__main__':
    input_dir = 'npc'
    output_dir = 'api'
    process_files(input_dir, output_dir)
