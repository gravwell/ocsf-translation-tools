import json
import os

def create_files_from_json(input_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print("Input file does not exist.")
        return

    # Open the input file
    with open(input_file, 'r') as f:
        data = f.read().strip().split('\n')
    
    # Create a directory to store individual JSON files
    output_dir = "output_files"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create individual JSON files
    for idx, json_str in enumerate(data):
        try:
            json_obj = json.loads(json_str)
            file_name = os.path.join(output_dir, f"json_{idx}.json")
            with open(file_name, 'w') as f:
                json.dump(json_obj, f, indent=4)
            print(f"Created file: {file_name}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON object at index {idx}: {e}")

# Replace 'input_file.txt' with the path to your input file
input_file = 'o365sample.json'
create_files_from_json(input_file)
