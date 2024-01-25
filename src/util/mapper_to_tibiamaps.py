import json
import requests
import os


# The URL or file path of the JSON file containing NPC data
NPC_JSON = "https://raw.githubusercontent.com/s2ward/tibia/main/api/npc_data.json"
# If the file is not a link, provide the file path like this:
# NPC_JSON = "path/to/npc_data.json"

# The name of the output JSON file with updated data
OUT_FILENAME = "npc_data.json"

# The zoom level for the tibiamaps.io link
TIBIAMAPS_ZOOM = 2;  # ranges from 0-4, where 4 is maximum zoom

# Function to convert the given URL to TibiaMaps coordinates
def fandomMapperToTibiaMaps(url):
    if url == "":
        return

    # Extract x, y, and z values from the URL
    x, y, z = url.split("=")[1].split("-")[:3]

    # Calculate Y-coordinate for tibiamaps.io
    Y = 31999
    y1, y2 = y.split(".")
    yn1 = int(y1) - 125
    yf = Y + int(y2) + (yn1 * 255) + yn1

    # Calculate X-coordinate for tibiamaps.io
    X = 32000
    x1, x2 = x.split(".")
    xn1 = int(x1) - 125
    xf = X + int(x2) + (xn1 * 255) + xn1

    # Return the calculated coordinates as integers
    return xf, yf, int(z)



# Check if NPC_JSON is a URL or a file path
if os.path.isfile(NPC_JSON):
    # If NPC_JSON is a file path, load data from the file
    with open(NPC_JSON, 'r') as json_file:
        data = json.load(json_file)
else:
    # If NPC_JSON is a URL, fetch JSON data from the URL
    response = requests.get(NPC_JSON)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to fetch data from {NPC_JSON}")
        exit()

# Process each item in the JSON data
for item in data:
    # Call the function and check if it returns a value
    coords = fandomMapperToTibiaMaps(item["map"])
    if coords:
        # If the function returns a value, unpack the coordinates
        xf, yf, z = coords
        item["tibiamap"] = f"https://tibiamaps.io/map#{xf},{yf},{z}:{TIBIAMAPS_ZOOM}"
        item["coords"] = [xf, yf, z]
    else:
        # If the function returns None, set tibiamap and coords to empty values
        item["tibiamap"] = ""
        item["coords"] = []

# Convert data back to JSON
output_json = json.dumps(data, indent=4)

# Save the updated JSON back to the file
with open(OUT_FILENAME, 'w') as json_file:
    json_file.write(output_json)
