import apache_beam as beam
import datetime
p1 = beam.Pipeline() 


filepath = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/Basics/input/bigquery_us-states_us-states.avro"

# Create a dictionary to store the metadata information
metadata_info = {
    "table": "table_name",
    "ingestion_start": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "ingestion_status": "In Progress",
    "ingested_file_summary": {}
}

try:
    data = {
        p1
        | "Reading Avro File" >> beam.io.ReadFromAvro(filepath)
        | beam.Ma(print)
    }
except Exception as e:
    print(f"Error in pipeline execution: {str(e)}")
    metadata_info["ingestion_status"] = "Error"


p1.run()