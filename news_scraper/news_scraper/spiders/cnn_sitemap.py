import scrapy


class CnnSitemapSpider(scrapy.Spider):
    name = 'cnn_sitemap'
    allowed_domains = ['cnn.com']
    start_urls = ['http://cnn.com/']

    def parse(self, response):
        pass
