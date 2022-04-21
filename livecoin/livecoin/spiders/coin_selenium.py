# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium_stealth import stealth


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['web.archive.org/web/20200116052415/https://www.livecoin.net/en']
    start_urls = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.headless = True

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        browser.set_window_size(1920, 1080)

        stealth(browser,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
            )

        # Open URL in browser
        browser.get("https://web.archive.org/web/20200116052415/https://www.livecoin.net/en")

        rur_tab = browser.find_elements(By.CLASS_NAME, "filterPanelItem___2z5Gb")
        rur_tab[4].click()

        self.html = browser.page_source
        browser.quit()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                "currency_pair": currency.xpath(".//div[1]/div/text()").get(),
                "volume(24h)": currency.xpath(".//div[2]/span/text()").get(),
            }
