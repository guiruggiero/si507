# 507 Homework 6 Part 2
# Developed by Gui Ruggiero

import requests
from bs4 import BeautifulSoup

#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Part 2 solution goes here

# Sample input: python3 hw6_part2-edited.py

user_agent = {'User-agent': 'Mozilla/5.0'}
html = requests.get("https://www.michigandaily.com", headers=user_agent).text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

searching_div = soup.find(class_='view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266')
#print(searching_div)
news_items = searching_div.find_all('li')
#print(news_items)
for li in news_items:
    print(li.string)