# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['duckduckgo.com', 'www.duckduckgo.com']
    start_urls = ['https://duckduckgo.com']

    def start_request(self):
        yield SeleniumRequest(
            url="https://duckduckgo.com",
            callback=self.parse,
            wait_time=3,
            screenshot=True,
        )

    def parse(self, response):
        inspect_response(response, self)
        # print(response.meta)
        # print(response.meta.keys())
        # img = response.meta["screenshot"]
        # print(f"This is the meta image: {img}")

        # with open("screenshot.png", "wb") as file:
        #     file.write(img)
