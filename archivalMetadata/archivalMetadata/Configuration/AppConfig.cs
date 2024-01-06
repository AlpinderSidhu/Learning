using System;
namespace archivalMetadata.Configuration
{
	public class AppConfig
	{
		public string ProjectId { get; set; }
		public string SubscriptionId { get; set; }
		public string BucketName { get; set; }
		public string ExcelFileName { get; set; }
		public string BigQueryDatasetId { get; set; }
		public string BigQueryTableId { get; set; }
	}
}

