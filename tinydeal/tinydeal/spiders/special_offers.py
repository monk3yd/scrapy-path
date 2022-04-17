# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        for item in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                "title": item.xpath(".//a[@class='p_box_title']/text()").get(),
                "url": response.urljoin(item.xpath(".//a[@class='p_box_title']/@href").get()),
                "special_price": item.xpath(".//div/span[@class='productSpecialPrice fl']/text()").get(),
                "normal_price": item.xpath(".//div/span[@class='normalprice fl']/text()").get()
            }
