# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        pass
