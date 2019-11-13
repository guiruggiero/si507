# SI 507 - final project, part 1
# Developed by Gui Ruggiero

import classes
import requests
from fake_useragent import UserAgent
from webbot import Browser # https://webbot.readthedocs.io/en/latest/
from bs4 import BeautifulSoup
import sqlite3

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

    # Storing in database
    conn = sqlite3.connect('divesites.sqlite')
    cur = conn.cursor()

    # Dropping tables
    statement = "DROP TABLE IF EXISTS 'Divesites';"
    cur.execute(statement)
    # print("\nTable 'Divesites' dropped (if existed)")

    # Other tables ...

    conn.commit()

    # Creating tables
    # Table 'Divesites' ...
    # statement = """
    #     CREATE TABLE 'Divesites' (
    #         'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
    #         'Company' TEXT NOT NULL,
    #         'SpecificBeanBarName' TEXT NOT NULL,
    #         'REF' TEXT NOT NULL,
    #         'ReviewDate' TEXT NOT NULL,
    #         'CocoaPercent' REAL NOT NULL,
    #         'CompanyLocationId' INTEGER NOT NULL,
    #         'Rating' REAL NOT NULL,
    #         'BeanType' TEXT,
    #         'BroadBeanOriginId' INTEGER NOT NULL,
    #     );
    # """
    cur.execute(statement)
    # print("Table 'Divesites' created")

    # Other tables ...

    conn.commit()

    # Inserting data
    # Table 'Divesites' ...
    # i = 0
    # for n in name:
    #     insertion = (None, alpha2[i], alpha3[i], name[i], region[i], subregion[i], population[i], area[i])
    #     statement = 'INSERT INTO "Countries" '
    #     statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    #     cur.execute(statement, insertion)
    #     i += 1

    # Other tables ...

    conn.commit()

    conn.close()

#scrape_scubaearth()