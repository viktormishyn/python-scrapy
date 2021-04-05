from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import NewsArticle


class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['https://edition.cnn.com/europe']

    # https://edition.cnn.com/2021/04/01/europe/who-europe-vaccine-program-slow-intl/index.html
    rules = [Rule(LinkExtractor(allow=r'\/2021\/[0-9][0-9]\/[0-9][0-9]\/[a-zA-Z\-]+\/[a-zA-z\-]+\/index.html'),
                  callback='parse', follow=True)]

    def parse(self, response):
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1[@class="pg-headline"]/text()').get()
        article['description'] = response.xpath('//meta[@itemprop="description"]/@content').get()
        article['body'] = response.xpath('//section[@data-zone-label="bodyText"]/div[@class="l-container"]//*/text()').getall()
        article['author'] = response.xpath('//meta[@itemprop="author"]/@content').get()
        article['datePublished'] = response.xpath('//meta[@itemprop="datePublished"]/@content').get()

        return article