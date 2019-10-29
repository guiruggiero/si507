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

# ----------------------------------------------
# Part 1: Get photo information using Flickr API
# ----------------------------------------------
print("----------------Part1--------------------")

# ----------------------------------------------
# Part 2: Map data onto Plotly
# ----------------------------------------------


