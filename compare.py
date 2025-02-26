import json
import os
from difflib import unified_diff

# Define the directory containing JSON files
json_dir = "/root/temp/data"

# Get all JSON files in the specified directory
json_files = sorted([f for f in os.listdir(json_dir) if f.endswith('.json')])

# Load JSON data from files
json_data = {}
for filename in json_files:
    filepath = os.path.join(json_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        try:
            json_data[filename] = json.load(file)
        except json.JSONDecodeError:
            print(f"Error: {filename} is not valid JSON.")
            json_data[filename] = None  # Mark as None to skip later

# Compare each file with every other file
for i in range(len(json_files)):
    for j in range(i + 1, len(json_files)):
        file1, file2 = json_files[i], json_files[j]

        if json_data[file1] is None or json_data[file2] is None:
            continue  # Skip invalid JSON files

        content1 = json.dumps(json_data[file1], indent=2, sort_keys=True)
        content2 = json.dumps(json_data[file2], indent=2, sort_keys=True)

        # Compute differences
        diff = list(unified_diff(content1.splitlines(), content2.splitlines(), fromfile=file1, tofile=file2, lineterm=''))

        if diff:
            print(f"--- Differences between {file1} and {file2} ---")
            print("\n".join(diff))
            print("\n")
        else:
            print(f"No differences found between {file1} and {file2}.")
