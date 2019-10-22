# 507 Homework 7 Part 1
# Developed by Gui Ruggiero

import requests
import json
from bs4 import BeautifulSoup

# Trying to load the cache from file
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# If no file, create a dictionary
except:
    CACHE_DICTION = {}

# Main cache function
def make_request_using_cache(url):
    unique_ident = url

    # Data already in cache?
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    # No - fetch data and add it to cache
    else:
        print("Making a request for new data...")
        resp = requests.get(url, headers={'User-Agent': 'SI_CLASS'})
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

#### Your Part 1 solution goes here ####

def get_umsi_data(page):
    for i in range(0,14):
        url_complement = "&page=" + i
        #print(url_complement)
        #print(page + url_complement)
        page_text = make_request_using_cache(page + url_complement)
        #print(page_text)
        page_soup = BeautifulSoup(page_text, 'html.parser')
        #print(page_soup)

        #get name and title
        #aaa

        #follow link to get email
        #aaa

        #write to dictionary
        #aaa

#### Execute function, get_umsi_data, here ####
url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All"
get_umsi_data(url)

#### Write out file here #####
#json = json.dumps(umsi_people)
#f = open("directory_dict.json", "w")
#f.write(json)
#f.close()