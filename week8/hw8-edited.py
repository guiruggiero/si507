# Developed by Gui Ruggiero

import requests
import json
import secret
import plotly
import plotly.graph_objs as go

# Caching file/dictionary
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

# Request/cache function for venue API
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

# Request/cache function for photo API
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

part2_data = []

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
        name = locations["response"]["venues"][i]["name"]
    except:
        name = "no name"    
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
        lat = locations["response"]["venues"][i]["location"]["lat"]
        lng = locations["response"]["venues"][i]["location"]["lng"]
    except:
        lat = 0
        lng = 0
    try:
        photo_id = photos["response"]["photos"]["items"][0]["id"]
    except:
        photo_id = "no photo"
    try:
        photo_url = photos["response"]["photos"]["items"][0]["prefix"] + "original" + photos["response"]["photos"]["items"][0]["suffix"]
    except:
        photo_url = "no photo"

    print("\nVenue", str(i+1) + ":", name)
    print("Address:", address + ",", city_response + ",", state, postal_code)
    print("Photo ID:", photo_id)
    #print("lat = ", lat)
    #print("lng = ", lng)

    # Storing relevant info for Part 2
    part2_data.append(dict(
        venue_name = name,
        venue_photo_url = photo_url,
        venue_lat = lat,
        venue_lng = lng
    ))
    #print(part2_data[i])

#print(part2_data)

# ----------------------------------------------
# Part 2: Map data onto Plotly
# ----------------------------------------------
print("\n----------------Part 2--------------------")

lat_vals = []
lgn_vals = []
text_vals = []
for i in part2_data:
    lat_vals.append(i["venue_lat"])
    lgn_vals.append(i["venue_lng"])
    text_vals.append("<br>"+i["venue_name"]+"<br>"+i["venue_photo_url"])

# Map style
layout = dict(
    title = "Top 25 results for '" + location_type + "' in '" + city + "'",
    autosize = True,
    hovermode = "closest",
    mapbox = dict(
        accesstoken = secret.MAPBOX_TOKEN,
        # center = dict(
        #     lat = 38,
        #     lon = -94
        # ),
        zoom = 3,
    )
)

fig = go.Figure(data = go.Scattermapbox(
    lat = lat_vals,
    lon = lgn_vals,
    text = text_vals,
    mode = 'markers',
    marker_color = 'blue',
    ))

fig.update_layout(layout)
fig.write_html('venues.html', auto_open = True)
print("\nMap created successfully!")