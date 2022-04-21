# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy.utils.log import configure_logging
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            callback=self.parse,
            screenshot=True,
        )

    def parse(self, response):
        img = response.meta["screenshot"]

        # Proof of work
        with open("screenshot.png", "wb") as file:
            file.write(img)
