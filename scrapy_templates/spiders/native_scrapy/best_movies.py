# -*- coding: utf-8 -*-
import unicodedata
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["www.web.archive.org", "web.archive.org"]
    start_urls = [
        "http://web.archive.org/web/20200715000935/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
    ]
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(
            url="http://web.archive.org/web/20200715000935/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating",
            headers={"User-Agent": self.user_agent},
        )

    rules = (
        # Allowed scrapable links
        # XPath
        Rule(
            LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"),
            callback="parse_item",
            follow=True,
            process_request="set_user_agent",
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"
            ),
            process_request="set_user_agent",
        ),
    )

    def set_user_agent(self, request):
        request.headers["User-Agent"] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            "title": unicodedata.normalize(
                "NFKD", response.xpath("//div[@class='title_wrapper']/h1/text()").get()
            ),
            "year": response.xpath("//span[@id='titleYear']/a/text()").get(),
            "duration": response.xpath("normalize-space((//time)[1]/text())").get(),
            "genre": response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            "rating": response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            "movie_url": response.url,
            # "user-agent": response.request.headers["User-Agent"],
        }