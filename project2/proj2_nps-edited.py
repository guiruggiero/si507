## proj_nps.py
## Developed by Gui Ruggiero

from secrets import google_places_key
import requests
import json
from bs4 import BeautifulSoup

# Caching file/dictionary
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

# Request/cache function
def make_request_using_cache(url):
    unique_ident = url

    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    
    else:
        #print("Making a request for new data...")
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()

        return CACHE_DICTION[unique_ident]

class NationalSite():
    def __init__(self, type_park, name, desc, url, street, city, state, zipcode):
        self.type = type_park
        self.name = name
        self.description = desc
        self.url = url
        self.address_street = street
        self.address_city = city
        self.address_state = state
        self.address_zip = zipcode

    def __str__(self):
        print(self.name + " (" + self.type + "): " + self.address_street + ", "
            + self.address_city + ", " + self.address_state + " " + self.address_zip)

class NearbyPlace():
    def __init__(self, name):
        self.name = name

## Must return the list of NationalSites for the specified state
## param: the 2-letter state abbreviation, lowercase
##        (OK to make it work for uppercase too)
## returns: list of all of the NationalSites
##        (e.g., National Parks, National Heritage Sites, etc.) that are listed
##        for the state at nps.gov
def get_sites_for_state(state_abbr):
    url = "https://www.nps.gov/state/" + state_abbr + "/index.htm"
    #print(url)
    state_text = make_request_using_cache(url)
    #print(state_text)
    state_soup = BeautifulSoup(state_text, "html.parser")
    #print(state_soup)
    parks_ul = state_soup.find(id = "list_parks").find_all(class_ = "clearfix")
    #print(parks_ul)
    i = 0
    for li in parks_ul:
        type_park = li.find("h2").text
        #print(type_park)
        name = li.find("h3").find("a").text
        #print(name)
        url_middle = li.find("h3").find("a")["href"]
        url = "https://www.nps.gov" + url_middle + "index.htm"
        #print(url)
        url_info = "https://www.nps.gov" + url_middle + "planyourvisit/basicinfo.htm"
        #print(url_info)
        description = li.find("p").text
        #print(description)

        park_info_text = make_request_using_cache(url_info)
        #print(park_info_text)
        park_info_soup = BeautifulSoup(park_info_text, "html.parser")
        #print(park_info_soup)
        # park_info = park_info_soup.find_all(itemprop = "address").find_all("span")
        park_info = park_info_soup.find(class_ = "physical-address-container")
        print(park_info)
        # for span in park_info:
        #     print(span.text)
        #     if span["itemprop"] == "streetAddress":
        #         street = span.text
        #     elif span["itemprop"] == "addressLocality":
        #         city = span.text
        #     elif span["itemprop"] == "addressRegion":
        #         state = span.text
        #     elif span["itemprop"] == "postalCode":
        #         zipcode = span.text
        # print(street)
        # print(city)
        # print(state)
        # print(zipcode)
        print("="*40)
        i = i + 1
    print(i)

## Must return the list of NearbyPlaces for the specific NationalSite
## param: a NationalSite object
## returns: a list of NearbyPlaces within 10km of the given site
##          if the site is not found by a Google Places search, this should
##          return an empty list
def get_nearby_places_for_site(national_site):
    return []

## Must plot all of the NationalSites listed for the state on nps.gov
## Note that some NationalSites might actually be located outside the state.
## If any NationalSites are not found by the Google Places API they should
##  be ignored.
## param: the 2-letter state abbreviation
## returns: nothing
## what it needs to do: launches a page with a plotly map in the web browser
def plot_sites_for_state(state_abbr):
    pass

## Must plot up to 20 of the NearbyPlaces found using the Google Places API
## param: the NationalSite around which to search
## returns: nothing
## what it needs to do: launches a page with a plotly map in the web browser
def plot_nearby_for_site(site_object):
    pass

get_sites_for_state("mi")