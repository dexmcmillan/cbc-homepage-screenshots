from selenium import webdriver
import datetime as dt
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True

options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--start-fullscreen')
options.add_argument("--start-maximized")
options.add_argument("--window-size=1080,1080")

today = dt.datetime.today().strftime("%Y-%m-%d_%H-%M")

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
browser.get("http://www.cbcnews.ca")

# get element 
featured = browser.find_element_by_class_name("featuredNewsContentPackage")
sidebar = browser.find_element_by_class_name("trendingList-sidebar")
  
# click screenshot 
featured.screenshot(f'screenshots/{today}-featured.png')
sidebar.screenshot(f'screenshots/{today}-sidebar.png')
browser.quit()