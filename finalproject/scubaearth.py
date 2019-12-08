# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

import classes
import requests
import json
from bs4 import BeautifulSoup
import sqlite3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# # # # # # # # # # # # # # # # # # # #
#                                     #
#   Part 1: Scraping ScubaEarth.com   #
#                                     #
# # # # # # # # # # # # # # # # # # # #

# # Initializing Selenium browser - Windows
# os.chmod(r"C:\Users\gui\Downloads\chromedriver.exe", 755)
# driver = webdriver.Chrome(executable_path=r"C:\Users\gui\Downloads\chromedriver.exe")

# # Initializing Selenium browser - Chrome OS
# os.chmod("/home/guilhermeruggiero/chromedriver", 755)
# driver = webdriver.Chrome(executable_path="/home/guilhermeruggiero/chromedriver")

# Country to be searched
country = "USA"

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
        CACHE_DICTION[url] = requests.get(url).text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[url]

def scrape_scubaearth():
    # try:
        # # Search page
        # driver.get("http://www.scubaearth.com/dive-site/dive-site-profile-search.aspx")
        # time.sleep(2)

        # # Typing country into the right field
        # field_location = driver.find_element_by_id("location")
        # field_location.clear()
        # field_location.send_keys(country)
        # time.sleep(2)

        # # Clicking search button        
        # button_search = driver.find_element_by_link_text("Search")
        # button_search.click()
        # time.sleep(7)
        
        # # Getting page source code
        # # results = driver.find_element_by_id("sites-tabs-result").get_attribute('innerText')
        # results = driver.page_source
        # results_json = json.dumps(results)
        
        # # Storing source code a file (Windows <> Chrome OS development)       
        # with open("page.json", "w") as file:
        #     file.write(results_json)
        
        # Reading source code from JSON file (Windows <> Chrome OS development)
        results_file = open("page.json", "r")
        results_json = results_file.read()
        results_soup = BeautifulSoup(results_json, "html.parser")
        # print(results_soup.prettify())

        # Finding div with results
        sites_div = results_soup.find(id='\\"sites-tabs-result\\"')
        # print(sites_div)
        site_list = sites_div.find_all("div")
        # print(site_list)

        # Going through every result and creating site objects
        sites = []
        for site_result in site_list:
            # print(site_result)
            # print(site_result.attrs)
            # print(site_result["class"])

            if site_result["class"] == ['\\"activity-module']:
                site_name = site_result.find("span").text.strip()
                # print(site_name)

            elif site_result["class"] == ['\\"dive-site-search-btns\\"']:
                site_url = "http://www.scubaearth.com" + site_result.find("a")["href"][2:-2]
                # print(site_url)

                # Fetching dive site page
                site_details = scraping_using_cache(site_url)
                # print(site_details)
                site_details_soup = BeautifulSoup(site_details, "html.parser")
                # print(site_details_soup.prettify())

                # site_location = 
                # site_notes = 
                # site_max_depth = 
                # site_notes = 
                # site_water = 
                # site_salinity = 

            else:
                data = site_result.text
                # print(data)
                site_lat = float(data[data.find(":") + 2:data.find(":") + 10])
                # print(site_lat)
                site_lgn = float(data[data.find("g") + 3:data.find("g") + 11])
                # print(site_lgn)

            # # Creating site object
            # new_site = Site(site_name, country)
            # new_site.lat = site_lat
            # new_site.lgn = site_lgn
            # new_site.location = site_location
            # new_site.notes = site_notes
            # new_site.max_depth = site_max_depth
            # new_site.notes = site_notes
            # new_site.water = site_water
            # new_site.salinity = site_salinity
            # sites.append(new_site)



        # # Storing in database
        # conn = sqlite3.connect('divelog.db')
        # cur = conn.cursor()

        # # Dropping tables
        # statement = "DROP TABLE IF EXISTS 'Sites';"
        # cur.execute(statement)
        # # print("Table 'Sites' dropped (if existed)")

        # conn.commit()

        # # Creating table
        # statement = """
        #     CREATE TABLE 'Sites' (
        #         'id' INTEGER PRIMARY KEY AUTOINCREMENT,
        #         'created_by' INTEGER,
        #         'name' TEXT NOT NULL,
        #         'country' TEXT NOT NULL,
        #         'location' TEXT,
        #         'lat' REAL,
        #         'lgn' REAL,
        #         'notes' TEXT,
        #         'picture' TEXT
        #     );
        # """
        # cur.execute(statement)
        # # print("Table 'Sites' created")

        # conn.commit()

        # # Inserting data
        # i = 0
        # for site in sites:
        #     insertion = (None, 1, site.name, site.location) # more stuff
        #     statement = "INSERT INTO 'Sites' "
        #     statement += "VALUES (?, ?, ?)"
        #     cur.execute(statement, insertion)
        #     i += 1

        # conn.commit()
        # # print("Data inserted into table 'Sites' successfully")

        # conn.close()

        # return True
    
    # except:
    #     return False

# Only runs when this file is run directly
if __name__=="__main__":
    scrape_scubaearth()
    pass