# SI 507 - final project, part 2
# Developed by Gui Ruggiero

import classes
import csv
import sqlite3
import secrets
import plotly.graph_objs as go
from statistics import mean

# # # # # # # # # # # # # # # # # # # #
#                                     #
#        Part 2: Importing CSV        #
#                                     #
# # # # # # # # # # # # # # # # # # # #

def import_divelog_csv()
    # Open file and get data
    f = open("divelog.csv")
    csv_data = csv.reader(f)

    # Create lists (change names, add)
    lat_vals = []
    lon_vals = []
    text_vals = []
    # ...

    # Extract data and build instances
    for row in csv_data:
        if row[0] != 'iata':
            lat_vals.append(row[5])
            lon_vals.append(row[6])
            text_vals.append(row[0])
    
    # Store in database
    conn = sqlite3.connect('dives.sqlite')
    cur = conn.cursor()
    #cur.execute("SELECT * FROM Employee")
    #for row in cur:
    #    print(row)
    # ...
    conn.close()

    # Plot dives into a map
    fig = go.Figure(data = go.Scattermapbox(
        lat = lat_vals,
        lon = lgn_vals,
        text = text_vals,
        mode = 'markers',
        marker_color = 'blue',
        )
    )
    layout = dict(
        title = "Dives",
        autosize = True,
        hovermode = "closest",
        mapbox = dict(
            accesstoken = secrets.MAPBOX_TOKEN,
            center = dict(
                lat = mean(lat_vals),
                lon = mean(lgn_vals)
            ),
            zoom = 11,
        )
    )
    fig.update_layout(layout)
    fig.write_html('dives.html', auto_open = True)

#import_divelog_csv()