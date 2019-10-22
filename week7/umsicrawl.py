import requests
from bs4 import BeautifulSoup

class CourseListing:
    def __init__(self, course_num, course_name):
        self.num = course_num
        self.name = course_name
    
    def __str__(self):
        course_str = self.num + ' - ' + self.name + '\n\n\t' + self.description + '\n\n' + self.prereq
        return course_str
    
    def init_from_details_prereq_url(self, details_url):
        page_text = requests.get(details_url, headers=header).text
        page_soup = BeautifulSoup(page_text, 'html.parser')
        self.description = page_soup.find(class_='course2desc').text
        self.prereq = page_soup.find(class_='course2prer').text

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = requests.get(catalog_url, headers=header).text
#print(page_text)
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

#content_div = page_soup.find_all(class_='view-content')
#print(len(content_div)) #to see if there's more than one
content_div = page_soup.find(class_='view-content')
#print(content_div)

table_rows = content_div.find_all('tr')
course_listings = []

for tr in table_rows[:5]:
    #print(tr)
    #print('-'*20)

    table_cells = tr.find_all('td')
    if len(table_cells) == 2:
        course_number = table_cells[0].text.strip()
        course_name = table_cells[1].text.strip()
        course_listing = CourseListing(course_number, course_name)

        details_url_end = table_cells[0].find('a')['href']
        details_url = baseurl + details_url_end
        course_listing.init_from_details_prereq_url(details_url)
        course_listings.append(course_listing)

#print(course_listings)
for cl in course_listings:
    print(cl)
    print("*"*50)