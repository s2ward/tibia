import json
import os

def parse_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    conversation, current_speaker, prompt, answers = [], None, None, []
    for line_number, line in enumerate(lines, 1):  # Start counting lines from 1
        if line.strip():
            try:
                speaker, text = line.split(':', 1)
                text = text.strip()
                if speaker == 'Player':
                    if current_speaker == speaker: 
                        prompt += " " + text
                    else:
                        if prompt is not None: 
                            conversation.append({'prompt': prompt, 'answer': answers})
                        prompt, answers = text, []
                else:
                    if current_speaker == speaker: 
                        answers.append(text)
                    else:
                        if answers: 
                            answers[-1] += " " + text
                        else: 
                            answers.append(text)
                current_speaker = speaker
            except ValueError:
                print(f"Error in file '{file_path}' at line {line_number}: '{line.strip()}'")
                raise  # Re-raises the last exception
    if prompt is not None: 
        conversation.append({'prompt': prompt, 'answer': answers})
    return conversation

def create_npc_data(file_path, name):
    conversation = parse_txt_file(file_path)
    return {'file': os.path.relpath(file_path), 'name': name, 'conversation': conversation}

def save_to_json(npc_data_list, output_file):
    with open(output_file, 'w') as file:
        json.dump(npc_data_list, file, indent=2)

def process_files(input_dir, output_dir):
    npc_data_list = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                npc_name = os.path.splitext(file)[0].replace(' ', '_')
                npc_data = create_npc_data(file_path, npc_name)
                npc_data_list.append(npc_data)
    output_file = os.path.join(output_dir, 'npc_transcript_database.json')
    save_to_json(npc_data_list, output_file)

if __name__ == '__main__':
    input_dir, output_dir = 'data/npcs/text', 'data/npcs'
    process_files(input_dir, output_dir)
