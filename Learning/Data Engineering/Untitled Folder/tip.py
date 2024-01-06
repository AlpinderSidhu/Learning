import json

# Specify the input JSONL file and output JSONL file
input_file = '/Users/alsidhu/Downloads/archive/JSONL/yelp_academic_dataset_tip.json'
output_file = '/Users/alsidhu/Downloads/archive/yelp_academic_dataset_tip.json'  # Change to your desired output file path

# Open the JSONL input file for reading and the output file for writing
with open(input_file, 'r') as jsonl_input_file, open(output_file, 'w') as jsonl_output_file:
    # Iterate through each line (record) in the JSONL input file
    for line in jsonl_input_file:
        # Parse the JSON object from the line
        data = json.loads(line)
        
        # Extract name and user_id
        business_id = data.get("business_id", None)
        user_id = data.get("user_id", None)
        
        # Create a new object with the remaining data
        remaining_data = {
            "business_id": business_id,
            "user_id": user_id,
            "tip_data": data,  # Store the remaining data as JSON string
        }
        
        # Serialize the remaining data as a JSON string and write it to the output JSONL file
        jsonl_output_file.write(json.dumps(remaining_data) + '\n')

print(f"Extracted data written to {output_file}")
