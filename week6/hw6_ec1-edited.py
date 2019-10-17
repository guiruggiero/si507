# 507 Homework 6 Extra Credit 1
# Developed by Gui Ruggiero

import requests
from bs4 import BeautifulSoup

#### Extra Credit 1 ####
print('\n*********** EXTRA CREDIT 1 ***********')
print('Top Headlines\n')

### Your Extra Credit 1 solution goes here

# Sample input: python3 hw6_ec1-edited.py

user_agent = {'User-agent': 'Mozilla/5.0'}
html = requests.get("https://www.michigandaily.com", headers=user_agent).text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

print('Top 5 Headlines: news')
div_news = soup.find(id='section-news')
#print(div_news)
news_items = div_news.find_all('a', class_=None)
#print(news_items)
#print(news_items[0])
for i in range(5):
    print(news_items[i].string)

# another option is to print every news_items.string, given that by the structure of the website there are "always" 5 headlines
#for a in news_items:
#    print(a.string)

print('\nTop 5 Headlines: sports')
div_sports = soup.find(id='section-sports')
sports_items = div_sports.find_all('a', class_=None)
for i in range(5):
    print(sports_items[i].string)

print('\nTop 5 Headlines: arts')
div_arts = soup.find(id='section-arts')
arts_items = div_arts.find_all('a', class_=None)
for i in range(5):
    print(arts_items[i].string)