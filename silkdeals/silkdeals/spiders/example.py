# -*- coding: utf-8 -*-
import logging
import scrapy
import time

from scrapy.selector import Selector
from scrapy.utils.log import configure_logging

from scrapy.shell import inspect_response

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from selenium_stealth import stealth


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.duckduckgo.com", "duckduckgo.com"]
    start_urls = ["https://duckduckgo.com"]

    def __init__(self):
        # Output log to file
        configure_logging(install_root_handler=False)
        logging.basicConfig(
            filename="scrapy_and_selenium_working_no_module.txt",
            format="%(levelname)s: %(message)s",
            level=logging.INFO,
        )

        chrome_options = Options()
        chrome_options.add_argument("start_maximized")
        chrome_options.headless = True

        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=chrome_options)
        self.browser.set_window_size(1920, 1080)

        stealth(
            self.browser,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

    def parse(self, response):
        self.browser.get(url="https://duckduckgo.com")
        time.sleep(3)
        self.browser.save_screenshot("screenshot.png")
