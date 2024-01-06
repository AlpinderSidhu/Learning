using System;
using archivalMetadata.Configuration;
using Microsoft.Extensions.Configuration;
using Google.Cloud.PubSub.V1;
using Grpc.Core;


namespace archivalMetadata.Services
{
	public class PubSubMessageHandler
	{

        private readonly ExcelProcessor _excelProcessor;
        private readonly BigQueryService _bigQueryService;
        private readonly AppConfig _appConfig;

        // Constructor with two arguments
        public PubSubMessageHandler(ExcelProcessor excelProcessor, BigQueryService bigQueryService, AppConfig appConfig)
        {
            _excelProcessor = excelProcessor ?? throw new ArgumentNullException(nameof(excelProcessor));
            _bigQueryService = bigQueryService ?? throw new ArgumentNullException(nameof(bigQueryService));
            _appConfig = appConfig ?? throw new ArgumentNullException(nameof(appConfig));
        }
        public void StartPullingMessages()
        {
            string projectId = _appConfig.ProjectId;
            string subscriptionId = _appConfig.SubscriptionId;

            
            SubscriptionName subscriptionName = SubscriptionName.FromProjectSubscription(projectId, subscriptionId);
            SubscriberServiceApiClient subscriberClient = SubscriberServiceApiClient.Create();
            int messageCount = 0;
            try
            {
                // Pull messages in a loop
                Console.WriteLine(subscriptionName);
                PullResponse response = subscriberClient.Pull(subscriptionName, maxMessages: 20);
                
                foreach (ReceivedMessage msg in response.ReceivedMessages)
                {
                    string text = System.Text.Encoding.UTF8.GetString(msg.Message.Data.ToArray());
                    Console.WriteLine($"Message {msg.Message.MessageId}: {text}");
                    Interlocked.Increment(ref messageCount);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error pulling and processing messages: {ex.Message}");
            }

        }
    }
}

