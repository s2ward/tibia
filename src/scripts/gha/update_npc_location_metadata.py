import os
import json
import sys

# Check if enough arguments are provided
if len(sys.argv) != 3:
    print("Usage: script.py <tibia/npc directory> <data/npcs/npc_metadata.json>")
    sys.exit(1)

# Use command-line arguments for the directory and JSON file path
root_dir = sys.argv[1]
json_file_path = sys.argv[2]

# Function to scan the directory structure and gather NPC information
def scan_directory_structure(root_dir):
    npc_structure = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                npc_name = file.replace('.txt', '')
                relative_path = os.path.relpath(root, root_dir)
                # Split the path, replace underscores with spaces, and handle null subareas
                parts = relative_path.split(os.sep)
                area, subarea = [(part.replace('_', ' ') if part else '') for part in (parts + [None, None])[:2]]
                # Ensure subarea is an empty string if None
                subarea = subarea if subarea is not None else ''
                npc_structure[npc_name] = {"area": area, "subarea": subarea}
    return npc_structure

# Function to update the JSON file based on the directory structure
def update_json_file(json_file_path, npc_structure):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    updated = False
    for npc in data:
        name = npc.get("name")
        if name in npc_structure:
            # Adjust location and subarea handling for underscore replacement and empty subarea
            npc_area = npc.get("location").replace('_', ' ') if npc.get("location") else None
            npc_subarea = npc.get("subarea").replace('_', ' ') if npc.get("subarea") else ''
            if npc_structure[name]["area"] != npc_area or npc_structure[name]["subarea"] != npc_subarea:
                npc["location"] = npc_structure[name]["area"]
                npc["subarea"] = npc_structure[name]["subarea"] if npc_structure[name]["subarea"] else ''
                updated = True
            del npc_structure[name]
     
    if updated:
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

# Main function to orchestrate the updating process
def main():
    npc_structure = scan_directory_structure(root_dir)
    update_json_file(json_file_path, npc_structure)
    print("NPC data JSON file has been updated.")

if __name__ == "__main__":
    main()
