from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pathlib import Path

# Initialize
chrome_path = Path(__file__).with_name("./chromedriver")
service = Service(chrome_path)
browser = webdriver.Chrome(service=service)

# Open URL in browser
browser.get("https://duckduckgo.com")

search_input = browser.find_element(By.ID, "search_form_input_homepage")
search_input.send_keys("My User Agent" + Keys.ENTER)

search_btn = browser.find_element(By.ID, "search_button_homepage")
search_btn.click()