from selenium import webdriver
import datetime as dt
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

today = dt.datetime.today().strftime("%Y-%m-%d_%H-%M")

browser = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
browser.get("http://www.cbcnews.ca")
browser.save_screenshot(f'screenshots/{today}.png')
browser.quit()