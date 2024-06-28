import json
import sys
import os
from datetime import datetime

# Function to count NPCs and calculate percentages
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

    # Creating output dictionary
    output = {
        "total_npcs": total_npcs,
        "verified": {
            "count": verified_count,
            "percentage": round(verified_percent, 2)
        },
        "unverified": {
            "count": unverified_count,
            "percentage": round(unverified_percent, 2)
        },
        "empty": {
            "count": empty_count,
            "percentage": round(empty_percent, 2)
        },
        "unverified_or_empty": {
            "count": unverified_count + empty_count,
            "percentage": round(unverified_or_empty_percent, 2)
        }
    }

    return output

# Function to get PR information
def get_pr_info():
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if event_path and os.path.exists(event_path):
        with open(event_path, 'r') as f:
            event_data = json.load(f)
        
        pr = event_data.get('issue', {}).get('pull_request', {})
        if pr:
            pr_number = event_data.get('issue', {}).get('number')
            pr_title = event_data.get('issue', {}).get('title')
            pr_url = pr.get('html_url')
            print("PR Number:", pr_number)
            print("PR Title:", pr_title)
            print("PR URL:", pr_url)
            return {
                'number': pr_number,
                'title': pr_title,
                'url': pr_url
            }
    return None

# Main execution
if __name__ == '__main__':
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else 'data/status/npc_verification_mapping.json'
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else 'data/status/npc_status.json'

    npc_stats = count_npcs(input_file_path)
    
    pr_info = get_pr_info()
    if pr_info:
        npc_stats['last_updated'] = {
            'date': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'pr_number': pr_info['number'],
            'pr_title': pr_info['title'],
            'pr_url': pr_info['url']
        }
    else:
        npc_stats['last_updated'] = {
            'date': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'pr_number': None,
            'pr_title': None,
            'pr_url': None
        }

    with open(output_file_path, 'w') as output_file:
        json.dump(npc_stats, output_file, indent=2)

    print(f"NPC status data has been written to {output_file_path}")
