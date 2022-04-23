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

        has_next = resp["has_next"]
        if has_next:
            next_page_number = resp["page"] + 1
            yield scrapy.Request(
                url=f"http://quotes.toscrape.com/api/quotes?page={next_page_number}",
                callback=self.parse,
            )
