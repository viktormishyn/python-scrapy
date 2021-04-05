import scrapy


class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['http://edition.cnn.com/']

    def parse(self, response):
        pass
