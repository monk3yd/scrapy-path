# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        items = response.xpath("//li[@class='productListing-even']")
        for item in items:
            item_title = item.xpath(".//a[@class='p_box_title']/text()").get()
            # item_price = item.xpath("//span[@")
            yield {
                "item": item_title
            }
