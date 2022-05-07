from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime as dt
import os

today = dt.datetime.today()

r = requests.get("https://www.cbc.ca/news").text

soup = BeautifulSoup(r, 'html.parser')
headlines = soup.find_all(class_="headline")

heads = []

for headline in headlines:
    heads.append(headline.contents)

heads = pd.DataFrame(heads)
heads["timestamp"] = today
heads = heads.set_index(0)

output_path='data/headlines.csv'
heads.to_csv(output_path, mode='a', header=not os.path.exists(output_path))