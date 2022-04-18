# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.glassesshop.com', 'glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div")
        for product in products:
            product_url = product.xpath(".//div[@class='product-img-outer']/a[1]/@href").get()
            product_image_link = product.xpath(".//div[@class='product-img-outer']/a[1]/img/@data-src").get()
            yield {
                "url": product_url,
                "image": product_image_link
            }
            # product_name =
            # product_price =
