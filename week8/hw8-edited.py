# Developed by Gui Ruggiero

import requests
import json
import secret
import plotly
import plotly.graph_objs as go

# Caching
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def request_using_cache_venue(city_query, location_type_query):
    #print(city_query+location_type_query)
    unique_ident = city_query + location_type_query
    #print(unique_ident)

    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    
    else:
        #print("Making a request for new data...")
        url = "https://api.foursquare.com/v2/venues/search"
        params = dict(
            client_id = secret.FOURSQUARE_ID,
            client_secret = secret.FOURSQUARE_SECRET,
            v = '20180323',
            near = city_query,
            query = location_type_query,
            limit = 25
        )
        resp = requests.get(url = url, params = params)
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()

        return CACHE_DICTION[unique_ident]

def request_using_cache_photo(id_query):
    unique_ident = id_query
    
    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    
    else:
        #print("Making a request for new data...")
        url = "https://api.foursquare.com/v2/venues/" + id_query + "/photos"
        params = dict(
            client_id = secret.FOURSQUARE_ID,
            client_secret = secret.FOURSQUARE_SECRET,
            v = '20180323',
            limit = 1
        )
        resp = requests.get(url = url, params = params)
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()

        return CACHE_DICTION[unique_ident]

# ----------------------------------------------
# Part 1: Get photo information using Foursquare API
# ----------------------------------------------
print("\n----------------Part 1--------------------\n")

city = input("In what city do you want to search? ")
location_type = input("What type of place are you looking for? ")

locations = request_using_cache_venue(city, location_type)
#print("\n", locations)

for i in range(25):
    venue_id = locations["response"]["venues"][i]["id"]
    photos = request_using_cache_photo(venue_id)
    #print(i)
    #print(locations["response"]["venues"][i]["name"])
    #print(photos)
    #try:
    #    print(photos["response"]["photos"]["items"][0]["id"], "\n")
    #except:
    #    print("No photo\n")

    # Handling if some information is missing
    try:
        address = locations["response"]["venues"][i]["location"]["address"]
    except:
        address = "no address"
    try:
        city_response = locations["response"]["venues"][i]["location"]["city"]
    except:
        city_response = "no city"
    try:
        state = locations["response"]["venues"][i]["location"]["state"]
    except:
        state = "no state"
    try:
        postal_code = locations["response"]["venues"][i]["location"]["postalCode"]
    except:
        postal_code = "no postal code"
    try:
        photo_id = photos["response"]["photos"]["items"][0]["id"]
    except:
        photo_id = "no photo"

    print("\nVenue", str(i+1) + ":", locations["response"]["venues"][i]["name"])
    print("Address:", address + ",", city_response + ",", state, postal_code)
    print("Photo ID:", photo_id)

# ----------------------------------------------
# Part 2: Map data onto Plotly
# ----------------------------------------------
#print("----------------Part 2--------------------")

#aaa