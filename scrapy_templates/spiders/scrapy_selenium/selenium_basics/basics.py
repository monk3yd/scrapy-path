from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium_stealth import stealth

# Initialize
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.headless = True

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

# Open URL in browser
browser.get("https://duckduckgo.com")

search_input = browser.find_element(By.ID, "search_form_input_homepage")
search_input.send_keys("My User Agent" + Keys.ENTER)

# search_btn = browser.find_element(By.ID, "search_button_homepage")
# search_btn.click()

print(browser.page_source)

browser.quit()
