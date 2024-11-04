from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
from csv import writer

driver = webdriver.Chrome()

url = "https://www.buzzfeed.com/tvandmovies"
driver.get(url)

news_links = []
news_titles = []

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(3)

data = BeautifulSoup(driver.page_source, 'html.parser')
for area in data.find_all('a', class_='js-card__link link-gray'):
    title = area.text
    link = area['href']
    news_titles.append(title)
    news_links.append(link)

with open('buzzfeed_news.csv','w', newline='', encoding='utf-8') as file:
    writer = writer(file)
    header = ['Title', 'Link']
    writer.writerow(header)
    for title, link in zip(news_titles, news_links):
        writer.writerow([title, link])

driver.quit()