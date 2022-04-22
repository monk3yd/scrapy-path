# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com', 'worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath("//table[@class='jsx-130793 table table-striped tp-table-body']/tbody/tr")
        for country in countries:
            name = country.xpath(".//td/a/text()").get()
            debt_to_gdp_ratio = country.xpath(".//td[2]/text()").get()
            yield {
                'name': name,
                'debt_to_gdp_ratio': debt_to_gdp_ratio
            }            
