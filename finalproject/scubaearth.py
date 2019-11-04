# SI 507 - final project, part 1
# Developed by Gui Ruggiero

import classes
import requests
from fake_useragent import UserAgent
from webbot import Browser # https://webbot.readthedocs.io/en/latest/
from bs4 import BeautifulSoup

# # # # # # # # # # # # # # # # # # # #
#                                     #
#   Part 1: Scraping ScubaEarth.com   #
#                                     #
# # # # # # # # # # # # # # # # # # # #

# Initializing fake user-agent and webbot browser
ua = UserAgent()
user_agent = {'User-agent': ua.chrome}

web = Browser()

# Caching file/dictionary
CACHE_FNAME = "cache.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

# Scraping with cache
def scraping_using_cache(url):
    if url in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[url]
    
    else:
        print("Making a request for new data...")
        CACHE_DICTION[url] = requests.get(url, headers = user_agent).text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[url]

def scrape_scubaearth()
    # Search page
    web.go_to("http://www.scubaearth.com/dive-site/dive-site-profile-search.aspx")
    web.type("united states", id = "location")
    web.click(text = "Search", tag = "a", )

    #for countries search
    #aaa

        #for rows results, scrape every page
        #aaa

    #store in database
    #aaa

#scrape_scubaearth()