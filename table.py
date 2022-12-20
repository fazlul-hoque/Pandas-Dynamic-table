

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/73437649/why-cant-beautifulsoup-find-a-table-on-this-webpage/73438169#73438169



import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options

webdriver_service = Service("./chromedriver") #Your chromedriver path
driver = webdriver.Chrome(service=webdriver_service)
url = 'https://www.stadiumgaming.gg/rank-checker?pokemon=WALREIN'
driver.get(url)
driver.maximize_window()
time.sleep(3)

table=BeautifulSoup(driver.page_source, 'lxml')

df = pd.read_html(str(table))[1]
print(df.iloc[1:,0:9])