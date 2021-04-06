import scrapy


class LoggingInSeleniumSpider(scrapy.Spider):
    name = 'logging_in_selenium'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass
