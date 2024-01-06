using archivalMetadata.Configuration;
using archivalMetadata.Services;
using Microsoft.Extensions.Configuration;
using System;

class Program
{
    static void Main1()
    {
        AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);

        // Load configuration from a config file or other source
        var config = LoadConfiguration();

        // Initialize PubSubMessageHandler, ExcelProcessor, and BigQueryService
        var excelProcessor = new ExcelProcessor(config);
        var bigQueryService = new BigQueryService(config);
        var pubSubMessageHandler = new PubSubMessageHandler(excelProcessor, bigQueryService, config);

        // Pull mexssages from Pub/Sub and trigger processing
        pubSubMessageHandler.StartPullingMessages();

        // PubSubMessageHandler.ProcessMessage should call ExcelProcessor.ProcessExcel
        // ExcelProcessor.ProcessExcel should call BigQueryService.InsertData
    }
    static AppConfig LoadConfiguration()
    {
        Console.WriteLine("Hiddd " + Directory.GetCurrentDirectory());
        IConfigurationRoot configuration = new ConfigurationBuilder()
            .SetBasePath(Path.Combine(Directory.GetCurrentDirectory(), "Configuration"))
            .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
            .Build();

        var appConfig = new AppConfig();

        Console.WriteLine("Hi" + configuration.GetSection("CustomSettings"));
        configuration.GetSection("CustomSettings").Bind(appConfig);

        return appConfig;
    }
}
