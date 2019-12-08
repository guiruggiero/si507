# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

import classes
import requests
from fake_useragent import UserAgent
import json
from bs4 import BeautifulSoup
import sqlite3

# # # # # # # # # # # # # # # # # # # #
#                                     #
#   Part 1: Scraping ScubaEarth.com   #
#                                     #
# # # # # # # # # # # # # # # # # # # #

'''
https://stackoverflow.com/questions/27869225/python-clicking-a-button-on-a-webpage/27869641
https://stackoverflow.com/questions/34504506/python-how-to-click-a-button-in-a-web-page-using-python
'''

# Initializing fake user-agent
ua = UserAgent()
user_agent = {'User-agent': ua.chrome}

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
        # print("Getting cached data...")
        return CACHE_DICTION[url]
    
    else:
        # print("Making a request for new data...")
        CACHE_DICTION[url] = requests.get(url, headers = user_agent).text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[url]

def scrape_scubaearth():
    try:
        # Search page - waiting on professor
        # web.go_to("http://www.scubaearth.com/dive-site/dive-site-profile-search.aspx")
        # web.type("united states", id = "location")
        # web.click(text = "Search", tag = "a", )

        sites = [] # list of objects. Append?
        i = 0
        #for rows results, scrape every page
            # url = aaa
            content = scraping_using_cache(url)
            # name = ???
            sites[i] = Site(name, "USA")
            # sites[i].location = ?
            # ...
            i += 1

        # Storing in database
        conn = sqlite3.connect('divelog.db')
        cur = conn.cursor()

        # Dropping tables
        statement = "DROP TABLE IF EXISTS 'Sites';"
        cur.execute(statement)
        # print("Table 'Sites' dropped (if existed)")

        conn.commit()

        # Creating table
        statement = """
            CREATE TABLE 'Sites' (
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'created_by' INTEGER,
                'name' TEXT NOT NULL,
                'country' TEXT NOT NULL,
                'location' TEXT,
                'lat' REAL,
                'lgn' REAL,
                'notes' TEXT,
                'picture' TEXT
            );
        """
        cur.execute(statement)
        # print("Table 'Sites' created")

        conn.commit()

        # Inserting data
        i = 0
        for site in sites:
            insertion = (None, 1, site.name, site.location) # more stuff
            statement = "INSERT INTO 'Sites' "
            statement += "VALUES (?, ?, ?)"
            cur.execute(statement, insertion)
            i += 1

        conn.commit()
        # print("Data inserted into table 'Sites' successfully")

        conn.close()

        return True
    
    except:
        return False