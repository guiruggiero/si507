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

# Using cache function
def external_data_using_cache(mode, url):
    unique_ident = url

    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    
    else:
        print("Making a request for new data...")

        if mode == "scrape":
            resp = requests.get(url)
            CACHE_DICTION[unique_ident] = resp.text
        elif mode == "api":
            resp = requests.get(url + "&key=" + google_places_key)
            CACHE_DICTION[unique_ident] = json.loads(resp.text)
        else:
            print("Mode not recognized, try again.")
        
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()

        return CACHE_DICTION[unique_ident]

class NationalSite():
    def __init__(self, type_park, name, desc = None, url = None, street = None, city = None, state = None, zipcode = None):
        self.type = type_park
        self.name = name
        self.description = desc
        self.url = url
        self.address_street = street
        self.address_city = city
        self.address_state = state
        self.address_zip = str(zipcode)

    def __str__(self):
        return self.name + " (" + self.type + "): " + self.address_street + ", " + self.address_city + ", " + self.address_state + " " + self.address_zip

class NearbyPlace():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def get_sites_for_state(state_abbr):
    parks = []
    
    url = "https://www.nps.gov/state/" + state_abbr + "/index.htm"
    #print(url)
    state_text = external_data_using_cache("scrape", url)
    #print(state_text)
    state_soup = BeautifulSoup(state_text, "html.parser")
    #print(state_soup)
    parks_ul = state_soup.find(id = "list_parks").find_all(class_ = "clearfix")
    #print(parks_ul)

    for li in parks_ul:
        try:
            type_park = li.find("h2").text.strip()
            #print(type_park)
        except:
            type_park = "no park type"
        name = li.find("h3").find("a").text
        #print(name)
        url_middle = li.find("h3").find("a")["href"]
        url = "https://www.nps.gov" + url_middle + "index.htm"
        #print(url)
        url_info = "https://www.nps.gov" + url_middle + "planyourvisit/basicinfo.htm"
        #print(url_info)
        description = li.find("p").text.strip()
        #print(description)

        park_info_text = external_data_using_cache("scrape", url_info)
        #print(park_info_text)
        park_info_soup = BeautifulSoup(park_info_text, "html.parser")
        #print(park_info_soup)
        try:
            street = park_info_soup.find(itemprop = "streetAddress").text.strip()
            #print(street)
        except:
            street = "no street address"
        city = park_info_soup.find(itemprop = "addressLocality").text.strip()
        #print(city)
        state = park_info_soup.find(itemprop = "addressRegion").text.strip()
        #print(state)
        zipcode = park_info_soup.find(itemprop = "postalCode").text.strip()
        #print(zipcode)
        #print(len(zipcode))

        park = NationalSite(type_park, name, description, url, street, city, state, zipcode)
        #print(park)
        parks.append(park)
    
    return parks

def get_nearby_places_for_site(national_site):
    places = []

    site_name = national_site.name
    #print(site_name)
    site_type = national_site.type
    #print(site_type)

    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + site_name + site_type + "&inputtype=textquery&fields=name,formatted_address,geometry"
    #print(url)

    place_search = external_data_using_cache("api", url)
    #print(place_search)
    #print(place_search["candidates"][0]["name"])
    #print(place_search["candidates"][0]["formatted_address"])
    try: # another option: if "status" != OK
        place_lat = place_search["candidates"][0]["geometry"]["location"]["lat"]
        #print(place_lat)
        place_lng = place_search["candidates"][0]["geometry"]["location"]["lng"]
        #print(place_lng)
    except:
        return places
    
    # Another option to check if Google Places does not return any results
    #if place_search["status"] != "OK":
    #    return places

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(place_lat) + "," + str(place_lng) + "&radius=10000"
    #print(url)

    nearby_places = external_data_using_cache("api", url)
    #print(nearby_places)
    nearby_places_results = nearby_places["results"]
    #print(nearby_places_results)
    for result in nearby_places_results:
        place_name = result["name"]
        #print(place_name)
        place = NearbyPlace(place_name)
        #print(place)
        places.append(place)
    
    return places

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

# Testing part 1
#print(len(get_sites_for_state("mi")))
#print(len(get_sites_for_state("az")))

# Testing part 2
#for i in get_nearby_places_for_site(NationalSite("National Monument", "Sunset Crater Volcano", "A volcano in a crater.")):
#    print(i)
#for i in get_nearby_places_for_site(NationalSite("National Park", "Yellowstone", "There is a big geyser there.")):
#    print(i)