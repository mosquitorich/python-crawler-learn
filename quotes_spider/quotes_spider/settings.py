BOT_NAME = "quotes_spider"

SPIDER_MODULES = ["quotes_spider.spiders"]
NEWSPIDER_MODULE = "quotes_spider.spiders"

ROBOTSTXT_OBEY = True

# ===== 反爬配置开始 =====
# 1. 下载延迟（秒）
DOWNLOAD_DELAY = 2

# 2. 每个域名的并发请求数（限制，避免过快）
CONCURRENT_REQUESTS_PER_DOMAIN = 4

# 3. 启用自动限速（AutoThrottle）
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# 4. 启用自定义下载中间件（随机 UA）
DOWNLOADER_MIDDLEWARES = {
    'quotes_spider.middlewares.RandomUserAgentMiddleware': 543,
}
# ===== 反爬配置结束 =====

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
