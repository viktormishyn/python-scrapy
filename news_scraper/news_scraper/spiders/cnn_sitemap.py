from scrapy.spiders import SitemapSpider
from news_scraper.items import NewsArticle


class CnnSpider(SitemapSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    sitemap_urls = ['https://www.cnn.com/sitemaps/article-2021-04.xml']

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