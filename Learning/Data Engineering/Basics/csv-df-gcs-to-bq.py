import apache_beam as beam
import os
import datetime
from apache_beam.options.pipeline_options import PipelineOptions

# Local Paths
local_input_path = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/Basics/input/dept_data.txt"
local_output_path = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/Basics/output/dept_data.txt"
# GCS paths
gcs_input_path = "gs://dataflow-bkt-001/input/dept_data.txt"
gcs_output_path = f"gs://dataflow-bkt-001/output/output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

service_account = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/data-engineering-396122-61d5312abdd9.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account

pipeline_options = {
    "project" : "data-engineering-396122",
    "runner" : "DataflowRunner",
    "region" : "us-central1",
    "staging_location": "gs://dataflow-bkt-001/temp",
    "temp_location":"gs://dataflow-bkt-001/temp_location",
    "template_location": "gs://dataflow-bkt-001/template/batch_job_df_gcs_bq_5",
    "save_main_session": True 
}
pipeline_options = PipelineOptions.from_dictionary(pipeline_options)
p1 = beam.Pipeline(options=pipeline_options)

# Table and Table Schema
bq_table = 'data-engineering-396122:dataset1.departments'
table_schema = 'employee_id:STRING, name:STRING, department_id:INTEGER, department:STRING, date:STRING'

def transform_to_dict(data):
    my_dict = {}
    my_dict['employee_id'] = data[0]
    my_dict['name'] = data[1]
    my_dict['department_id'] = data[2]
    my_dict['department'] = data[3]
    my_dict['date'] = data[4]
    return(my_dict)

get_data = {
    p1
    | "Import Data" >> beam.io.ReadFromText(gcs_input_path) 
    | "Splitting Data" >> beam.Map(lambda r : (r.split(",")))
    | "Filtering Data" >> beam.Filter(lambda record: (record[3] == "Accounts"))
    | "Transforming To Dictionary" >> beam.Map(lambda record: transform_to_dict(record))
    | "Writing Data" >> beam.io.WriteToBigQuery(
        bq_table,
        schema=table_schema,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        custom_gcs_temp_location="gs://dataflow-bkt-001/temp"
        )
}

p1.run()