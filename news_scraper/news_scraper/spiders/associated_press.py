import scrapy


class AssociatedPressSpider(scrapy.Spider):
    name = 'associated_press'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']

    def parse(self, response):
        pass
