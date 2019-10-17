# 507 Homework 6 Part 1
# Developed by Gui Ruggiero

import requests
import sys
from bs4 import BeautifulSoup

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("-------Alt tags-------\n")

### Your Part 1 solution goes here

# Sample input: python3 hw6_part1-edited.py http://newmantaylor.com/gallery.html

url = sys.argv[1]
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

all_img_tags = soup.find_all('img')
#print(all_img_tags)
for img in all_img_tags:
    #print(img)
    #print(img['alt'])
    try:
        print(img['alt'])
    except:
        print("No alternative text provided!")