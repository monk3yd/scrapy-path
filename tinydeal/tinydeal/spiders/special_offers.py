# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.web.archive.org', 'web.archive.org']
    start_urls  = ["https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html"]

    def start_request(self):
        yield scrapy.Request(
                url="https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html",
                callback=self.parse,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
                } 
            )

    def parse(self, response):
        for item in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield {
                "title": item.xpath(".//a[@class='p_box_title']/text()").get(),
                "url": response.urljoin(item.xpath(".//a[@class='p_box_title']/@href").get()),
                "special_price": item.xpath(".//div/span[@class='productSpecialPrice fl']/text()").get(),
                "normal_price": item.xpath(".//div/span[@class='normalprice fl']/text()").get(),
                "User-Agent": response.request.headers["User-Agent"]
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
                })
