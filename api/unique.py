import json

def extract_unique_words(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract all words from the conversations
    words = set()
    for npc in data:
        conversations = npc.get("conversation", [])
        for convo in conversations:
            # Extracting words from prompts
            words.update(convo.get("prompt", "").split())

            # Extracting words from answers
            for answer in convo.get("answer", []):
                words.update(answer.split())

    # Sorting the unique words
    sorted_unique_words = sorted(words)
    return sorted_unique_words

# Replace 'your_file_path_here' with the actual path of your JSON file
file_path = '/home/s2w/tibia-clean/tibia/api/conversations.json'
unique_words = extract_unique_words(file_path)

# Printing the sorted unique words
for word in unique_words:
    print(word)
