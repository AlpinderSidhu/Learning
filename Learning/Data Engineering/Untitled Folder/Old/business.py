import apache_beam as beam
import json

p2 = beam.Pipeline()
filename = 'input.json'
batch_size = 2  # Change batch size to 2
json_objects = []

class grouping_objects(beam.DoFn):
    def process(self, element):
        json_obj = json.loads(element)
        json_objects.append(json_obj)
        
        if len(json_objects) == batch_size:
            json_object = {"data1": json_objects}
            yield beam.window.TimestampedValue(json_object, 0)  # Use TimestampedValue
            json_objects.clear()  # Clear the list for the next batch

    def finish_bundle(self):
        # Handle any remaining JSON objects
        if json_objects:
            json_object = {"data1": json_objects}
            yield beam.window.TimestampedValue(json_object, 0)  # Use TimestampedValue

input_data = (
    p2
    | "Reading" >> beam.io.ReadFromText(filename, coder=beam.coders.BytesCoder())
    | "Grouping File" >> beam.ParDo(grouping_objects())
    | beam.io.WriteToText("output.json", file_name_suffix=".json", shard_name_template='')
)

p2.run()
