import scrapy
import json


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=12']

    def __init__(self):
        CONST = 12
        self.ebook_counter = CONST

    def parse(self, response):
        resp = json.loads(response.body)
        ebooks = resp["works"]
        for ebook in ebooks:
            yield {
                "title": ebook["title"],
                "subject": ebook["subject"]
            }
        if self.ebook_counter == CONST:
            self.max_ebook_count = resp["ebook_count"]

        if int(self.ebook_counter) <= self.max_ebook_count:
            self.ebook_counter = str(int(self.ebook_counter) + CONST)
            yield scrapy.Request(
                url=f"https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.ebook_counter}",
                callback=self.parse
            )
