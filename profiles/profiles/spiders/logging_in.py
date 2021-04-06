import scrapy


class LoggingInSpider(scrapy.Spider):
    name = 'logging_in'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass
