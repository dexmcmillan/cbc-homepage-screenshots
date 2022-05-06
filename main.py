from selenium import webdriver
import datetime as dt
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True

options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

today = dt.datetime.today().strftime("%Y-%m-%d_%H-%M")

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
browser.get("http://www.cbcnews.ca")
browser.save_screenshot(f'screenshots/{today}.png')
browser.quit()