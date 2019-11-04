## Developed by Gui Ruggiero

from secrets import google_places_key, MAPBOX_TOKEN
import requests
import json
from bs4 import BeautifulSoup
import plotly
import plotly.graph_objs as go
from statistics import mean

# Caching file/dictionary
CACHE_FNAME = "cache.json"
try:
    cache_file = open(CACHE_FNAME, "r")
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

# Using cache function
def external_data_using_cache(mode, url):
    unique_ident = url

    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    
    else:
        #print("Making a request for new data...")

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
    def __init__(self, name, lat = 0, lgn = 0):
        self.name = name
        self.lat = lat
        self.lgn = lgn

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

    place_coordinates = get_place_coordinates(national_site)
    #print(place_coordinates)
    if place_coordinates == None:
        return []
    else:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + place_coordinates + "&radius=10000"
        #print(url)

        nearby_places = external_data_using_cache("api", url)
        #print(nearby_places)
        nearby_places_results = nearby_places["results"]
        #print(nearby_places_results)
        for result in nearby_places_results:
            place_name = result["name"]
            #print(place_name)
            place_lat = result["geometry"]["location"]["lat"]
            #print(place_lat)
            place_lgn = result["geometry"]["location"]["lng"]
            #print(place_lgn)
            place = NearbyPlace(place_name, place_lat, place_lgn)
            #print(place)
            places.append(place)
        
        return places

def get_place_coordinates(national_site):

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
        return None
    
    # Another option to check if Google Places does not return any results
    #if place_search["status"] != "OK":
    #    return None

    return str(place_lat) + "," + str(place_lng)

def plot_sites_for_state(state_abbr):
    lat_vals = []
    lgn_vals = []
    text_vals = []
    
    sites = get_sites_for_state(state_abbr)
    #print(sites)

    for site in sites:
        #print(site)
        site_coordinates = get_place_coordinates(site)
        #print(site_coordinates)
        if site_coordinates == None:
            #print(site.name)
            pass
        else:
            comma = site_coordinates.find(",")
            #print(comma)
            lat = float(site_coordinates[:comma])
            #print(lat)
            lgn = float(site_coordinates[comma+1:])
            #print(lgn)
            lat_vals.append(lat)
            lgn_vals.append(lgn)
            text_vals.append("<br>" + site.name)

    #if len(lat_vals) == len(lgn_vals) and len(lat_vals) == len(text_vals):
    #    print(len(lat_vals))
    #else:
    #    print(len(lat_vals))
    #    print(len(lgn_vals))
    #    print(len(text_vals))

    # Map data
    fig = go.Figure(data = go.Scattermapbox(
        lat = lat_vals,
        lon = lgn_vals,
        text = text_vals,
        mode = "markers",
        marker_color = "blue",
        marker_size = 15,
        )
    )

    # Map style
    layout = dict(
        title = "National sites in " + state_abbr.upper(),
        autosize = True,
        hovermode = "closest",
        mapbox = dict(
            accesstoken = MAPBOX_TOKEN,
            center = dict(
                lat = mean(lat_vals),
                lon = mean(lgn_vals)
            ),
            zoom = 5.5,
        )
    )

    # Map creation and showing
    fig.update_layout(layout)
    fig.write_html("state_sites.html", auto_open = True)
    print("\nMap 'state_sites.html' created successfully! Open your browser to view it.\n")

def plot_nearby_for_site(site_object):
    lat_vals = []
    lgn_vals = []
    text_vals = []
    
    nearby_places = get_nearby_places_for_site(site_object)
    #print(len(nearby_places))
    #print(nearby_places)

    if nearby_places == []:
        print("\nThe map was not created, the coordinates of the national site were not found.\n")
        return
    else:
        for place in nearby_places:
            if place.lat == 0:
                #print(place.name)
                pass
            else:
                #print(place.lat)
                lat_vals.append(place.lat)
                #print(place.lgn)
                lgn_vals.append(place.lgn)
                #print(place.name)
                text_vals.append("<br>" + place.name)
        
        #if len(lat_vals) == len(lgn_vals) and len(lat_vals) == len(text_vals):
        #   print(len(lat_vals))
        #else:
        #   print(len(lat_vals))
        #   print(len(lgn_vals))
        #   print(len(text_vals))
        
        # Map data
        fig = go.Figure(data = go.Scattermapbox(
            lat = lat_vals,
            lon = lgn_vals,
            text = text_vals,
            mode = "markers",
            marker_color = ["blue", "black"],
            marker_size = 15,
            )
        )

        # Map style
        layout = dict(
            title = "Places near " + site_object.name,
            autosize = True,
            hovermode = "closest",
            mapbox = dict(
                accesstoken = MAPBOX_TOKEN,
                center = dict(
                    lat = mean(lat_vals),
                    lon = mean(lgn_vals)
                ),
                zoom = 11,
            )
        )

        # Map creation and showing
        fig.update_layout(layout)
        fig.write_html("nearby_site.html", auto_open = True)
        print("\nMap 'nearby_site.html' created successfully! Open your browser to view it.\n")

# Testing part 1
#print(len(get_sites_for_state("mi")))
#print(len(get_sites_for_state("az")))

# Testing part 2
#for i in get_nearby_places_for_site(NationalSite("National Monument", "Sunset Crater Volcano", "A volcano in a crater.")):
#    print(i)
#for i in get_nearby_places_for_site(NationalSite("National Park", "Yellowstone", "There is a big geyser there.")):
#    print(i)

# Testing part 3
#plot_sites_for_state("mi")
#plot_sites_for_state("az")
#plot_nearby_for_site(NationalSite("National Monument", "Sunset Crater Volcano", "A volcano in a crater."))
#plot_nearby_for_site(NationalSite("National Park", "Yellowstone", "There is a big geyser there."))

# Part 4
command = input("\nCiao! Enter a command or 'help' for options: ").strip()

while command != "exit":
    if command == "help":
        print("\nHere is a list of commands you can use:\n")
        print("   list <state_abbr>")
        print("       available anytime")
        print("       lists all National Sites in a state")
        print("       valid inputs: a two-letter state abbreviation")
        print("   nearby <result_number>")
        print("       available only if there is an active site list")
        print("       list all Places nearby a given result")
        print("       valid inputs: an integer 1-len(result_set_size)")
        print("   map <option>")
        print("       available only if there is an active site or nearby result list")
        print("       displays the current results on a map")
        print("   exit")
        print("       exits the program")
        print("   help")
        print("       lists all available commands (these instructions)\n")
    
    elif command[:4] == "list":
        state = command[-2:]
        print("\nNational Sites in " + state.upper() + "\n")
        sites = get_sites_for_state(state)
        i = 1
        for site in sites:
            print(i, site)
            i = i + 1
        print("\nNow you can type:")
        print("   - 'nearby <result_number>' to view places near one of the sites above")
        print("   - 'map sites' to view the site list above on a map")
        print("   - 'list <state>” to do a search for another state\n")
    
    elif command[:6] == "nearby":
        try:
            chosen_site = int(command[7:])-1
            print("\nPlaces near " + sites[chosen_site].name + "\n")
            places = get_nearby_places_for_site(sites[chosen_site])
            i = 1
            for place in places:
                print(i, place)
                i = i + 1
            print("\nNow you can type:")
            print("   - 'map nearby' to view the nearby list above on a map")
            print("   - 'nearby <result_number>' to view places near another site")
            print("   - 'map sites' to view the last site list on a map")
            print("   - 'list <state>” to do a search for another state\n")
        except:
            print("\n*** You need a site list first. Try typing 'list <state>'.\n")
    
    elif command[:3] == "map":
        if command[4:] == "sites":
            try:
                plot_sites_for_state(state)
            except:
                print("\n*** You need a site list first. Try typing 'list <state>'.\n")
        elif command[4:] == "nearby":
            try:
                plot_nearby_for_site(sites[chosen_site])
            except:
                print("\n*** You need a nearby list first. Try typing 'nearby <result_number>' (if you already have a site list).\n")
        else:
            print("\n*** Sorry, I did not understand your command. Please try again.\n")
    
    else:
        print("\n*** Sorry, I did not understand your command. Please try again.\n")
        
    command = input("Enter a command or 'help' for options: ").strip()

print("\nThanks for using this program. Arrivederci! :-)\n")