using System;
using archivalMetadata.Configuration;

namespace archivalMetadata.Services
{
	public class ExcelProcessor
	{
        private readonly AppConfig _appConfig;

        public ExcelProcessor(AppConfig appConfig)
		{
            _appConfig = appConfig ?? throw new ArgumentNullException(nameof(appConfig));
        }
	}
}

