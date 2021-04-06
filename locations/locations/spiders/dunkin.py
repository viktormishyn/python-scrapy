import scrapy


class DunkinSpider(scrapy.Spider):
    name = 'dunkin'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['http://dunkindonuts.com/']

    def parse(self, response):
        pass
