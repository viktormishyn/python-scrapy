import scrapy
import json


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get()
        title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        number = response.xpath('//span[@class="rfc-no"]/text()').get()
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        text = response.xpath('//div[@class="text"]').get()
        headings = response.xpath('//span[@class="subheading"]/text()').getall()

        author_name = response.xpath('//meta[@name="DC.Creator"]/@content').get()
        author_company = response.xpath('//span[@class="author-company"]/text()').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        phone = response.xpath('//span[@class="phone"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()

        d = {"title": title, "number": number, "date": date, "description": description, "text": text,
             "headings": headings,
             "author": {"author_name": author_name, "author_company": author_company,
                        "address": address, "phone": phone, "email": email}}

        return d
