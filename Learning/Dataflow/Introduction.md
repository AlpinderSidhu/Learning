Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Use Dataflow to create data pipelines that read from one or more sources, transform the data, and write the data to a destination.

Dataflow is one of the runner for Beam that is provided by Google/GCP

- Dataflow uses the same programming model for both batch and stream analytics.
- Dataflow allows you to execute your Beam pipelines on Google Cloud. -> Dataflow is built on the open-source Apache Beam project. Apache Beam lets you write pipelines using a language-specific SDK. Currently, Apache Beam supports Java, Python, and Go SDKs, as well as multi-language pipelines.
  Dataflow executes Apache Beam pipelines. If you decide later to run your pipeline on a different platform, such as Apache Flink or Apache Spark, you can do so without rewriting the pipeline code.
- It is fully managed and autoconfigured. When you run a Dataflow job, the Dataflow service allocates a pool of worker VMs to execute the pipeline. You don't need to provision or manage these VMs. When the job completes or is cancelled, Dataflow automatically deletes the VMs. You're billed for the compute resources that your job uses.
- Dataflow is designed to support batch and streaming pipelines at large scale. Data is processed in parallel, so the work is distributed across multiple VMs.
- Dataflow supports several different ways to create and execute pipelines, depending on your needs:
  - Write code using the Apache Beam SDKs.
  - Deploy a Dataflow template. Templates let you run pre-defined pipelines. For example, a developer can create a template, and then a data scientist can deploy it on demand.
    Google also provides a library of templates for common scenarios. You can deploy these templates without knowing any Apache Beam programming concepts.
  - Use JupyterLab notebooks to develop and run pipelines iteratively.
