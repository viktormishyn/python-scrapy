import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']

    def parse(self, response):
        pass
