from google.cloud import bigquery
import json

# Set your Google Cloud project ID
project_id = "db-record-mgmt"
dataset_id = "transformed_yelp_json"
table_id = "tip_1"
table_address=  f"{project_id}.{dataset_id}.{table_id}"
# Initialize the BigQuery client
client = bigquery.Client(project=project_id)



# Open the JSONL file for reading
with open('/Users/alsidhu/Downloads/archive/JSONL/yelp_academic_dataset_tip.json', 'r') as jsonl_file:
    # Iterate through each line (record) in the JSONL file
    for line in jsonl_file:
        # Parse the JSON object from the line
        data = json.loads(line)
        
        business_id = data.get("business_id", None)
        user_id = data.get("user_id", None)
        
        # Create a BigQuery row from the data
        row = {
            "business_id": business_id,
            "user_id": user_id,
            "tip_data": json.dumps(data),  # Store the remaining data as JSON string
        }

        # Insert the row into the table using streaming inserts
        errors = client.insert_rows_json(table_address, [row])

        if not errors:
            print(f"Data inserted into {project_id}.{dataset_id}.{table_id}")
        else:
            print("Encountered errors while inserting data:")
            for error in errors:
                print(error)