import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        resp = json.loads(response.body)
        quotes = resp["quotes"]
        for quote in quotes:
            yield {
                "author": quote["author"]["name"],
                "quote_text": quote["text"],
                "tags": quote["tags"],
            }
