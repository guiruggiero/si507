import requests
import json
from bs4 import BeautifulSoup

class CourseListing:
    def __init__(self, course_num, course_name):
        self.num = course_num
        self.name = course_name
    
    def __str__(self):
        course_str = self.num + ' - ' + self.name + '\n\n\t' + self.description + '\n\n' + self.prereq
        return course_str
    
    def init_from_details_prereq_url(self, details_url):
        page_text = make_request_using_cache(details_url, header)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        self.description = page_soup.find(class_='course2desc').text
        self.prereq = page_soup.find(class_='course2prer').text

# On startup, try to load the cache from file
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# If there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}

# The main cache function: it will always return the result for this url.
# However, it will first look to see if we have already cached the result
# and, if so, return the result from cache. If we haven't cached the
# result, it will get a new one (and cache it)
def make_request_using_cache(url, header):
    unique_ident = url

    # First, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    # If not, fetch the data afresh, add it to the cache,
    # then write the cache to file
    else:
        print("Making a request for new data...")
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

baseurl = 'https://www.si.umich.edu'
catalog_url = baseurl + '/programs/courses/catalog'
header = {'User-Agent': 'SI_CLASS'}
page_text = make_request_using_cache(catalog_url, header)
#print(page_text)
page_soup = BeautifulSoup(page_text, 'html.parser')
#print(page_soup)

#content_div = page_soup.find_all(class_='view-content')
#print(len(content_div)) #to see if there's more than one
content_div = page_soup.find(class_='view-content')
#print(content_div)

table_rows = content_div.find_all('tr')
course_listings = []

for tr in table_rows[:25]:
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