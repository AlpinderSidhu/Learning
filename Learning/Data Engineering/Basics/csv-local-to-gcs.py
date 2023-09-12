import apache_beam as beam
import os
import datetime

service_account = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/data-engineering-396122-61d5312abdd9.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account

input_path = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/Basics/input/dept_data.txt"
# Output Path
local_path = "/Users/alsidhu/git-repos/asingh/Learning/Learning/Data Engineering/Basics/output/dept_data.txt"
gcs_path = f"gs://dataflow-bkt-001/output_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"



p1 = beam.Pipeline()

get_data = {
    p1
    | "Import Data" >> beam.io.ReadFromText(input_path) 
    | beam.Map(lambda r : (r.split(",")))
    | beam.Filter(lambda record: (record[3] == "Accounts"))
    | beam.Map(print)
    | beam.io.WriteToText(gcs_path)
}

p1.run()

 