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
            item_special_price = item.xpath(".//div/span[@class='productSpecialPrice fl']/text()").get()
            item_normal_price = item.xpath(".//div/span[@class='normalprice fl']/text()").get()

            yield {
                "item_title": item_title,
                "item_special_price": item_special_price,
                "item_normal_price": item_normal_price
            }
