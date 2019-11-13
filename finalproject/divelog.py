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
    f.close()

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
            # ...
    
    # Storing in database
    conn = sqlite3.connect('dives.sqlite')
    cur = conn.cursor()

    # Dropping tables
    statement = "DROP TABLE IF EXISTS 'Dives';"
    cur.execute(statement)
    # print("\nTable 'Dives' dropped (if existed)")

    # Other tables ...

    conn.commit()

    # Creating tables
    # Table 'Dives' ...
    # statement = """
    #     CREATE TABLE 'Dives' (
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
    # print("Table 'Dives' created")

    # Other tables ...

    conn.commit()

    # Inserting data
    # Table 'Dives' ...
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

    # Plot dives into a map
    # text vals ...
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
            zoom = 11, # how to determine programmatically?
        )
    )
    fig.update_layout(layout)
    fig.write_html('dives.html', auto_open = True)

#import_divelog_csv()