import json
import sys

def count_npcs(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_npcs = 0
    verified_count = 0
    unverified_count = 0
    empty_count = 0

    for city in data.values():
        for location, npcs in city.items():
            if isinstance(npcs, dict):  # For subareas
                for status in npcs.values():
                    total_npcs += 1
                    if status == "VERIFIED":
                        verified_count += 1
                    elif status == "UNVERIFIED":
                        unverified_count += 1
                    elif status == "EMPTY":
                        empty_count += 1
            else:  # For direct NPCs under main area
                total_npcs += 1
                if npcs == "VERIFIED":
                    verified_count += 1
                elif npcs == "UNVERIFIED":
                    unverified_count += 1
                elif npcs == "EMPTY":
                    empty_count += 1

    # Calculating percentages
    verified_percent = (verified_count / total_npcs) * 100 if total_npcs > 0 else 0
    unverified_percent = (unverified_count / total_npcs) * 100 if total_npcs > 0 else 0
    empty_percent = (empty_count / total_npcs) * 100 if total_npcs > 0 else 0
    unverified_or_empty_percent = ((unverified_count + empty_count) / total_npcs) * 100 if total_npcs > 0 else 0

    # Creating output string
    output = f"Total NPCs: {total_npcs}\n"
    output += f"Verified: {verified_count}/{total_npcs}, {verified_percent:.2f}%\n"
    output += f"Unverified: {unverified_count}/{total_npcs}, {unverified_percent:.2f}%\n"
    output += f"Empty: {empty_count}/{total_npcs}, {empty_percent:.2f}%\n"
    output += f"Unverified or Empty: {unverified_count + empty_count}/{total_npcs}, {unverified_or_empty_percent:.2f}%"

    return output

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = 'api/file_mapping.json'
