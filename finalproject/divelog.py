# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

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

class Dive():
    def __init__(self, start_date, start_time, total_time, max_depth):
        self.diver = 1
        self.site = 0
        
        self.start_date = start_date
        self.start_time = start_time # how to format and attribute?
        self.total_time = total_time
        self.max_depth = max_depth
        
        self.start_pressure = 0
        self.end_pressure = 0
        self.surface_temp = 0
        self.bottom_temp = 0
        self.weights = 0
        self.dive_center = "dive_center"
        self.boat = "boat"
        self.structures = "structures"
        self.animals = "animals"
        self.rating = 0
        self.favorite = False
        self.photo_album = "photo_album"
        self.notes = "notes"
        self.validated = False
        self.gas = "gas"
        self.share_oxygen = 0.0
        self.share_nitrogen = 0.0
        self.share_helium = 0.0
        self.surface_supplied = False
        self.bottom_type = "bottom"
        self.transportation = "transportation"
        self.entry = "entry" # giant step, backroll, etc.
        self.drift = False
        self.night = False
        self.deep = False
        self.wreck = False
        self.cave = False
        self.ice = False
        self.altitude = False
        self.decompression = False
        self.rescue = False
        self.photo = False
        self.training = False
        self.buddy = "buddy"
        self.stop_depth = 0.0
        self.stop_duration = 0

    def __str__(self):
        return self.diver + " @ " + self.site + " (" + self.start_date + ")"

def import_divelog_csv():
    # Open file and get data
    f = open("divelog.csv")
    csv_data = csv.reader(f)
    f.close()

    dives = []
    i = 0
    # Extract data and build instances
    for row in csv_data:
        if row[i] != 'dive':
            dives[i] = Dive() # start_date, start_time, total_time, max_depth
            i += 1
    
    # Storing in database
    conn = sqlite3.connect('divelog.db')
    cur = conn.cursor()

    # Dropping tables
    statement = "DROP TABLE IF EXISTS 'Dives';"
    cur.execute(statement)
    # print("\nTable 'Dives' dropped (if existed)")

    conn.commit()

    # Creating table - varbinary, date, time
    statement = """
        CREATE TABLE 'Dives' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'diver' INTEGER NOT NULL,
            'site' INTEGER NOT NULL,
            'start_date' date NOT NULL
            'start_time' time NOT NULL,
            'total_time' INTEGER NOT NULL,
            'max_depth' REAL NOT NULL,
            'start_pressure' INTEGER,
            'end_pressure' INTEGER,
            'surface_temp' REAL,
            'bottom_temp' REAL,
            'weights' INTEGER,
            'dive_center' TEXT,
            'boat' TEXT,
            'structures' TEXT,
            'animals' TEXT,
            'rating' INTEGER,
            'favorite' varbinary,
            'album' TEXT,
            'notes' TEXT,
            'validated' varbinary,
            'gas' TEXT,
            'share_oxygen' REAL,
            'share_nitrogen' REAL,
            'share_helium' REAL,
            'surface_supplied' varbinary,
            'transportation' TEXT,
            'water' TEXT,
            'body' TEXT,
            'entry' TEXT,
            'drift' varbinary,
            'night' varbinary,
            'deep' varbinary,
            'wreck' varbinary,
            'cave' varbinary,
            'ice' varbinary,
            'altitude' varbinary,
            'decompression' varbinary,
            'rescue' varbinary,
            'photo' varbinary,
            'training' varbinary,
            'buddy' TEXT,
            'stop_depth' REAL,
            'stop_duration' INTEGER
            FOREIGN KEY(site) REFERENCES sites(id);
        );
    """

    cur.execute(statement)
    # print("Table 'Dives' created")

    conn.commit()

    # Inserting data
    i = 0
    # for n in name:
    #     insertion = (None, alpha2[i], alpha3[i], name[i], region[i], subregion[i], population[i], area[i])
    #     statement = 'INSERT INTO "Countries" '
    #     statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    #     cur.execute(statement, insertion)
    #     
    #     lat_vals.append(row[5])
    #     lgn_vals.append(row[6])
    #     text_vals.append(row[0])
    # 
    #     i += 1

    conn.commit()
    # print("Data inserted into table 'Dives' successfully")

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

# Only runs when this file is run directly
if __name__=="__main__":
    import_divelog_csv()
    pass