import scrapy
from scrapy_selenium import SeleniumRequest


class TestSpider(scrapy.Spider):
    name = 'test'

    def start_request(self):
        yield SeleniumRequest(
            url='https://www.geeksforgeeks.org/',
            wait_time=3,
            callback=self.parse,
            screenshot=True,
        )

    def parse(self, response):
        img = response.meta["screenshot"]
        # inspect_response(response, self)

        # Proof of work
        with open("screenshot.png", "wb") as file:
            file.write(img)
