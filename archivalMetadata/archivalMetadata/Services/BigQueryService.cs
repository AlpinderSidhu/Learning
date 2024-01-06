using System;
using archivalMetadata.Configuration;
using archivalMetadata.Services;
using Microsoft.Extensions.Configuration;

namespace archivalMetadata.Services
{
	public class BigQueryService
	{
        private readonly AppConfig _appConfig;

        public BigQueryService(AppConfig appConfig)
		{
            _appConfig = appConfig ?? throw new ArgumentNullException(nameof(appConfig));
        }
	}
}