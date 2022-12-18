# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:63342/main.py/html_pages/hmm.html?_ijt=5rmfu9edbmv2jmpnh7o4oj3vl2'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find('p', class_='demo_1')

print(quotes)