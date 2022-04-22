# -*- coding: utf-8 -*-
import time
import logging
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from scrapy.utils.log import configure_logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        # Proof of work
        # with open("screenshot.png", "wb") as file:
        #     file.write(response.meta["screenshot"])

        browser = response.meta["driver"]
        search_input = browser.find_element(By.ID, "search_form_input_homepage")
        search_input.send_keys("Hello World" + Keys.ENTER)

        time.sleep(3)

        browser.save_screenshot("enter.png")

        html = browser.page_source  # When getting elements with selenium (line 29) the original response from SeleniumRequest is modified
        response_obj = Selector(text=html)
        links = response_obj.xpath("//div[@class='result__extras__url']/a")
        for link in links:
            yield {
                "URL": link.xpath(".//@href").get()
            }
