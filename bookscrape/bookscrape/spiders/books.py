# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        book_name = response.xpath("//@title").get()
        book_price = response.xpath("//p[@class='price_color']/text()").get()
        yield {
            "name": book_name,
            "price": book_price
        }
