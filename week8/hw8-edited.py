# Developed by Gui Ruggiero

import requests
import json
import secret
import plotly
import plotly.graph_objs as go

# Don't change this part
FLICKR_KEY = secret.FLICKR_KEY
MAPBOX_TOKEN = secret.MAPBOX_TOKEN

base_url = "https://api.flickr.com/services/rest"
'''
 Compose the url for requests to use.
 Parameters:
    method: string. The API method you want to use. e.g. "flickr.galleries.getInfo"
    parameter: dictionary. The parameters for the API query. e.g. {"gallery_id": "72157617483228192"}
 Returns: string. A composed url for requests to use. 
'''
def compose_url(method, parameter):
    temp_list = []
    for i in parameter:
        temp_list.append(str(i) + "=" + str(parameter[i]).replace(" ", "+"))
    parameter_string = "&".join(temp_list)
    return base_url+"/?method={}&api_key={}&{}&format=json&nojsoncallback=1".format(method, FLICKR_KEY, parameter_string)

# -----------------------------------------------------------------------------

# Caching
CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def make_request_using_cache(method, parameter):
    unique_ident = parameter["city"]
    if unique_ident in CACHE_DICTION:
        #print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        #print("Making a request for new data...")
        resp = requests.get(compose_url(method, parameter))
        
#       change value to only the list of photo information your API got 
        CACHE_DICTION[unique_ident] = resp.text

        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

# ----------------------------------------------
# Part 1: Get photo information using Flickr API
# ----------------------------------------------
print("----------------Part 1--------------------")

# Sample input: python3 hw8.py Ann Arbor
query = sys.argv[1]

# get place_id from city
#aaa

# get 250 photos from place_id
#aaa

# filter out the photos uploaded by the same person (only one photo per uploader should be kept)
#AAA

# print stuff out
# Photo id: 45375804911
# Title:
# Description:
#aaa

# ----------------------------------------------
# Part 2: Map data onto Plotly
# ----------------------------------------------
print("----------------Part 2--------------------")

#aaa