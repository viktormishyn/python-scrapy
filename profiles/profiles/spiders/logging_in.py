import scrapy


class LoggingInSpider(scrapy.Spider):
    name = 'logging_in'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']

    def make_requests_from_url(self, url):
        # to add cookies to the request we should modify the scrapy request object before it is sent.
        # in order to do this we should overwrite the make_request_from_url method, used by scrapy.Spider
        request = super(LoggingInSpider, self).make_requests_from_url(url)
        request.cookies['username'] = 'ryan'
        request.cookies['loggedin'] = '1'
        return request

    def parse(self, response):
        return {'text': response.xpath('//body/text()').get()}
