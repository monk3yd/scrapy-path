# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        self.page_num = 1

        yield SeleniumRequest(
            url="http://quotes.toscrape.com/js",
            wait_time=3,
            callback=self.parse,
            screenshot=True
        )

    def parse(self, response):
        # Init browser
        browser = response.meta["driver"]

        # Scrape quote_text, author, all_tags for each quote from all pages
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                "quote": quote.xpath(".//span[@class='text']/text()").get(),
                "author": quote.xpath(".//small[@class='author']/text()").get(),
                "tags": quote.xpath(".//div[@class='tags']/a/text()").getall()
            }

        # Next page
        next_page = response.xpath("//li[@class='next']/a")
        if next_page:
            absolute_url = f"http://quotes.toscrape.com/js/page/{self.page_num}/"
            self.page_num += 1
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )
        # Proof of work
        # with open("screenshot_computer_deal.png", "wb") as file:
        #     file.write(response.meta["screenshot"])
