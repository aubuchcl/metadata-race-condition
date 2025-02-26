import json
import os
from deepdiff import DeepDiff  # Install with: pip install deepdiff

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

# Function to fully sanitize DeepDiff results for JSON serialization
def make_serializable(obj):
    """Recursively converts DeepDiff objects (PrettyOrderedSet, frozenset, etc.) into JSON-serializable types."""
    if isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (set, frozenset)) or "PrettyOrderedSet" in str(type(obj)):  
        # Convert any set (including PrettyOrderedSet) to a list
        return list(obj)
    elif isinstance(obj, list):  # Recursively handle lists
        return [make_serializable(v) for v in obj]
    elif hasattr(obj, "to_dict"):  # Convert DeepDiff objects that support `.to_dict()`
        return make_serializable(obj.to_dict())
    else:
        return obj  # Return the object if it’s already serializable

# Compare each file with every other file
for i in range(len(json_files)):
    for j in range(i + 1, len(json_files)):
        file1, file2 = json_files[i], json_files[j]

        if json_data[file1] is None or json_data[file2] is None:
            continue  # Skip invalid JSON files

        # Use DeepDiff to compare the two JSON files
        diff = DeepDiff(json_data[file1], json_data[file2], ignore_order=True)

        if diff:
            print(f"\n--- Differences between {file1} and {file2} ---")
            print(json.dumps(make_serializable(diff), indent=2))  # Fully sanitize before printing
        else:
            print(f"No differences found between {file1} and {file2}.")
