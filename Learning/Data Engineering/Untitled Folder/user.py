import json

# Specify the input JSONL file and output JSONL file
input_file = '/Users/alsidhu/Downloads/archive/JSONL/yelp_academic_dataset_user.json'
output_file = '/Users/alsidhu/Downloads/archive/yelp_academic_dataset_user.json'  # Change to your desired output file path

# Open the JSONL input file for reading and the output file for writing
with open(input_file, 'r') as jsonl_input_file, open(output_file, 'w') as jsonl_output_file:
    # Iterate through each line (record) in the JSONL input file
    for line in jsonl_input_file:
        # Parse the JSON object from the line
        data = json.loads(line)
        
        # Extract name and user_id
        name = data.get("name", None)
        user_id = data.get("user_id", None)
        
        # # Remove name and user_id from the data dictionary
        # if "name" in data:
        #     del data["name"]
        # if "user_id" in data:
        #     del data["user_id"]
        
        # Create a new object with the remaining data
        remaining_data = {
            "name": name,
            "user_id": user_id,
            "user_data": data
        }
        
        # Serialize the remaining data as a JSON string and write it to the output JSONL file
        jsonl_output_file.write(json.dumps(remaining_data) + '\n')

print(f"Extracted data written to {output_file}")
