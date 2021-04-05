import scrapy


class CnnAllArticlesSpider(scrapy.Spider):
    name = 'cnn_all_articles'
    allowed_domains = ['cnn.com']
    start_urls = ['http://cnn.com/']

    def parse(self, response):
        pass
