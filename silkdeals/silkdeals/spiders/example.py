# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy.utils.log import configure_logging
# from scrapy.shell import inspect_response
from scrapy_selenium import SeleniumRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'

    # allowed_domains = ['duckduckgo.com', 'www.duckduckgo.com']
    # start_urls = ['https://duckduckgo.com']

    # Output log to file
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def start_request(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            callback=self.parse_result,
            wait_time=3,
            screenshot=True,
        )

    def parse_result(self, response):
        # inspect_response(response, self)
        img = response.meta["screenshot"]
        # print(f"This is the meta image: {img}")

        # Proof of work
        with open("screenshot.png", "wb") as file:
            file.write(img)
