package com.db.df.beam.core.pipeline;

import com.db.df.beam.core.options. PubsubToQPipelineOptions;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryI0; import org.apache.beam.sdk.io.gcp.bigquery.InsertRetryPolicy; import org.apache.beam.sdk.io.gcp.bigquery.WriteResult; import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options. PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.windowing.Fixedblindows;
import org.apache.beam.sdk.transforms .windowing .Window;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.PCollectionTuple;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
import org.apache.beam.sdk.transforms. ParDo;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.Don. ProcessElement;
import org.apache.beam.sdk.transforms.DoFn.Element;
import org.apache.beam.sdk.transforms.Don.OutputReceiver;
import org.apache.beam.sdk.transforms. Reshuffle;
import org.apache.avro.generic.GenericRecord;
import org.apache.beam.sdk.io.AvroI0; import org.apache.beam.sdk.io.FileIO;
import org.apache.beam. sdk. transforms.SerializableFunction;
import org.joda.time.Duration;
import org.sif4j. Logger;
import org.slf4j.LoggerFactory;
import org.apache.beam.sdk.coders.AvroCoder;
import org.apache.avro.schema.Parser;
import org.apache.beam.sdk.coders.StringUtf8Coder;

import org.apache.beam.sdk.coders.AtomicCoder;
import java.util.concurrent. ConcurrentHashMap;
import java.io.OutputStream;
import java.io.I0Exception;
import java.io.InputStream;
import org.apache.beam.sdk. schemas .SchemaRegistry;
import org.apache.avro.Schema. Parser;
import java.util.List;
import java.util.Arraylist;
import java.util.Map;
import java.util. HashMap;
import com.google.api.services.bigquery.model. TableRow;
import com.google.api.services.bigquery.model. TableSchema;
import com.google.api.services.bigquery.model.TableFieldSchema;
import com.google.common.collect. ImmutableList;
import java.io.Serializable;
import java. time. Instant;
import static org.apache.beam.sdk.io.gcp.bigquery.BigQueryI0.Write.CreateDisposition.CREATE_NEVER;
import static org.apache.beam.sdk.io.gcp.bigquery.BigQueryIo.Write.WriteDisposition.WRITE_APPEND;





public class PubsubToBQPipeline {
    private static final Logger logger = LoggerFactory.getLogger(PubsubToBQPipeline.class);

    public static void main(String[] args) throws Throwable {
        PubsubToBQPipelineOptions options = PipelineOptionsFactory.fromArgs(args).withValidation().as(PubsubToBQPipelineOptions.class);
        options.setworkerMachineType(options.getMachine().get());
        
        Pipeline p = Pipeline.create (options);

        PCollection<String> gcsPaths = p.apply("ReadPubSubSubscription", PubsubIO.readMessagesWithAttributes().fromSubscription(options.getPubSubSubscription()))
        .apply("Get GCS path", ParDo.of (new DoFn<PubsubMessage, String> () {
            @ProcessElement
            public void processElement(@Element PubsubMessage message, OutputReceiver<String> receiver) {
                try {
                    logger.info("PubSub Message: " + message.toString());
                    String objectId = message.getAttribute("objectId");
                    if (objectId.endswith(".avro")) {
                        String bucketId = message.getAttribute("bucketId");
                        String cloudStoragePath = String.format("gs://%s/%s", bucketId, objectId);
                        logger. info("Cloud Storage Path: " + cloudStoragePath);
                        receiver.output (cloudStoragePath);
                    } else {
                        logger. info("Skipping object: " + objectId);
                    }
                } catch (Exception e) {
                    logger. info(e.getMessage ());
                }
            }
        }));
        
        String avroSchema = "{}"

        Pcollection<AvroModel[]> dataAvro =
        gesPaths.apply ("Read avro files", FileIO.matchAll ())
        .apply (FileIO.readMatches ())
        .apply (AvroIO.readFiles (AvroModel[].class));


        PCollection<BigQueryInsertRow> dataForBQ = dataAvro.apply("Create Table Row", ParDo.of (new DoFn<AvroModel[], BigQueryInsertRow>() {
        @ProcessElement
        public void processElement (@Element AvroModel[] messages, OutputReceiver<BigQueryInsertRow> receiver) {
            for (int 1 = 0; 1 < messages.length; 1+÷)
            {
            //logger.info"Avro Message " + i + " message
            BigQueryInsertRow tableRow = new BigQueryInsertRow();
            tableRow.data = messages[i].Data;
            tableRow.insertId = messages[i].Id;
            tableRow.source = messages[i].DataSource:
            tableRow.fileld = messages[i].FileId;
            tableRow.partitionDate = messages[i].PartitionDate:
            tableRow.clusterKey = messages[i].ClusterKey;
            tableRow.version = messages[i].Version;
            tableRow.creationTime = Instant.now();
            receiver.output (tableRow);
        }
        }
        }));


        WriteResult writeResult = dataForBQ.apply("WriteRecordsToBQ", BigQueryI0. ‹BigQueryInsertRow›write()
        .withMethod(BigQueryI0.Write.Method.STORAGE_WRITE_API)
        .withFormatFunction(item -> new TableRow() .set("insertId", item.insertId)
        .set ("data", item.data)
        .set ("source", item.source)
        .set ("fileId", item.fileId)
        .set ("creationTime".item.creationTime)
        .set ("partitionDate", item.partitionDate)
        .set("clusterKey", item.clusterKey)
        .set ("version", item. version))
        .withSchema (new TableSchema ().setFields(
            ImmutableList.of (
                new TableFieldSchema().setName("InsertId").setType("STRING"),
                new TableFieldSchema().setName("data").setType("JSON"),
                new TableFieldSchema().setName("source").setType("STRING"),
                new TableFieldSchema().setName("fileId").setType("STRING"),
                new TableFieldSchema().setName("creationTime").setType("TIMESTAMP"),
                new TableFieldSchema().setName("partitionDate").setType("DATE"),
                new TableFieldSchema ().setName("clusterKey").setType ("STRING"),
                new TableFieldSchema ().setName("version").setType("INTEGER")
        )))
        .withFailedInsertRetryPolicy(InsertRetryPolicy.retryTransientErrors())//Retryallfailuresexceptforknownpersistenterrors.
        .withWriteDisposition(WRITE_APPEND)
        .withCreateDisposition(CREATE_NEVER)
        .withTriggeringFrequency(Duration.standardSeconds(15))
        // .withExtendedError Info ()
        .withNumStorageWriteApiStreams(15)
        .withoutValidation ()
        .optimizedWrites()
        .to(options getOutputTable())
        );
        p.run();
    }
}

class AvroModel implements Serializable {
    String Id;
    String Data;
    String FileId;
    String DataSource;
    String PartitionDate;
    String ClusterKey;
    Integer Version;
    public boolean equals (Object other) {
        return ((AvroModel) other).Id.equals(Id);
    }
}

class BigQueryInsertRow implements Serializable {
    String insertId;
    String data;
    Instant creationTime;
    String source;
    String fileId;
    String partitionDate;
    String clusterKey;
    Integer version;
    
    public boolean equals (Object other) {
        return ( (BigQueryInsertRow) other).insertId.equals (insertId);
    }
}

class GenericRecordCoder extends AtomicCoder<GenericRecord> {
    public static GenericRecordCoder of() {
        return new GenericRecordCoder();
    }

    private static final ConcurrentHashMap<String, AvroCoder<GenericRecord>> avroCoders = new ConcurrentHashMap<>();

    @Override
    public void encode(GenericRecord value, OutputStream outStream) throws IOException {
        String schemaString = value.getSchema().toString();
        String schemaName = value.getSchema().getFulLName();
        StringUtf8Coder.of().encode(schemaString, outStream);
        StringUtf8Coder.of().encode(schemaName, outStream);
        AvroCoder<GenericRecord› coder = avroCoders.computeIfAbsent(schemaName,
        s -> AvroCoder.of(value.getSchema()));
        coder.encode(value,outStream);
    }

    @override
    public GenericRecord decode (InputStream inStream) throws IOException {
        String schemaString = StringUtf8Coder.of().decode(inStream);
        String schemaHash = StringUtf8Coder.of().decode(inStream);
        AvroCoder<GenericRecord> coder = avroCoders.computeIfAbsent(schemaHash,
        s -> AvroCoder.of(new Parser().parse(schemaString)));
        return coder.decode(inStream);
    }
}