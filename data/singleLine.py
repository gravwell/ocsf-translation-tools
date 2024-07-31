import json
import sys

def single_line_json(json_objects):
    return [json.dumps(obj) for obj in json_objects]


def read_multiline_json_objects(file_path):
    json_objects = []
    current_json = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            current_json += line
            # Count opening and closing braces to determine if we have a complete JSON object
            if current_json.count('{') == current_json.count('}'):
                try:
                    json_objects.append(json.loads(current_json))
                    current_json = ""
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue
    return json_objects

def main(input_file, output_file):
    json_objects = read_multiline_json_objects(input_file)
    single_line_json_objects = single_line_json(json_objects)

    with open(output_file, 'w') as outfile:
        for obj in single_line_json_objects:
            outfile.write(obj + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python singleLine.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
