import scrapy
from scrapy_selenium import SeleniumRequest
import time


def wait(driver):
    time.sleep(1)
    return True


class LoggingInSpider(scrapy.Spider):
    name = 'logging_in'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/login.html']

    def make_requests_from_url(self, url):
        # to add cookies to the request we should modify the scrapy request object before it is sent.
        # in order to do this we should overwrite the make_request_from_url method, used by scrapy.Spider
        return SeleniumRequest(url=url, wait_time=10, wait_until=wait)

    def parse(self, response):
        driver = response.request.meta['driver']

        username = driver.find_element_by_xpath('//input[@name="username"]')
        # username object
        username.send_keys('ryan')
        password = driver.find_element_by_xpath('//input[@name="password"]')
        password.send_keys('password')

        submit = driver.find_element_by_xpath('//input[@type="submit"]')
        submit.click()
        time.sleep(2)

        profile_link = driver.find_element_by_xpath('//a[@href="profile.php]')
        profile_link.click()
        time.sleep(2)

        return {'text': response.xpath('//body/text()').get()}
