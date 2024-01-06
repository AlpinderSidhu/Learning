import json
with open('business_input.json', 'r') as input_business_file:
    new_objects = []
    for line in input_business_file:
        # Parse the JSON object from the line
        data = json.loads(line)
        # Extract business_id and name
        business_id = data.get('business_id', None)
        name = data.get('name', None)
        # Remove business_id and name from the original data
        if 'business_id' in data:
            del data['business_id']
        if 'name' in data:
            del data['name']
        # Create a new object with the remaining data
        new_object = {
            'business_id': business_id,
            'name': name,
            'other_data': data  # You can change 'other_data' to a more appropriate name
        }
        
        # Append the new object to the list
        new_objects.append(new_object)

# Write the new data to a new JSONL file
with open('business_output.json', 'w') as output_business_file:
    for new_object in new_objects:
        # Serialize the new object as a JSON string and write it to the new JSONL file
        output_business_file.write(json.dumps(new_object) + '\n')
