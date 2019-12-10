# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

import csv
import datetime
import sqlite3
import secret
import plotly.graph_objs as go
from statistics import mean

# # # # # # # # # # # # # # # # # # # #
#                                     #
#        Part 2: Importing CSV        #
#                                     #
# # # # # # # # # # # # # # # # # # # #

class Dive():
    def __init__(self, num, site, start_date, start_time, total_time, max_depth):
        self.diver = 1

        self.num = num
        self.site = site
        self.start_date = start_date
        self.start_time = start_time
        self.total_time = total_time
        self.max_depth = max_depth
        
        self.location = "location"
        self.country = "country"
        self.lat = 0.0
        self.lgn = 0.0
        self.gas = "gas"
        self.buddy = "buddy"
        self.bottom_temp = 0
        self.dive_center = "dive_center"
        self.boat = "boat"
        self.notes = "notes"

    def __str__(self):
        return str(self.diver) + " @ " + self.site + " (" + self.country + ")"

def import_divelog_csv():
    # Open file and get data
    f = open("dives.csv")
    csv_data = csv.reader(f)
    # print(csv_data)
    print("\n10. File opened and imported\n")

    dives = []
    # Extract data and build instances
    for row in csv_data:
        if row[0] != "Num":
            # print(row)
            dive_date = datetime.datetime(int(row[2]), int(row[3]), int(row[4]))
            # print(dive_date)
            dive = Dive(int(row[0]), row[1], dive_date, row[5], int(row[6]), float(row[7]))
            
            dive.location = row[8]
            dive.country = row[9]
            dive.gas = row[13]
            dive.buddy = row[14]
            dive.dive_center = row[15]
            dive.boat = row[16]
            dive.notes = row[17]

            try:
                dive.lat = float(row[10])
            except:
                dive.lat = row[10]

            try:
                dive.lgn = float(row[11])
            except:
                dive.lgn = row[11]

            try:
                dive.bottom_temp = int(row[12])
            except:
                dive.bottom_temp = row[12]
            
            # print(dive)
            dives.append(dive)

    # print(dives)
    f.close()
    print("11. Data extracted - total: " + str(len(dives)) + "\n")
 
    # Storing in database
    conn = sqlite3.connect("divelog.db")
    cur = conn.cursor()

    # Dropping table
    statement = "DROP TABLE IF EXISTS 'Dives';"
    cur.execute(statement)
    conn.commit()
    print("12. Table 'Dives' dropped (if present)\n")

    # Creating table
    statement = """
        CREATE TABLE 'Dives' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'diver' INTEGER NOT NULL,
            'num' INTEGER NOT NULL,
            'site' TEXT NOT NULL,
            'start_date' TEXT NOT NULL,
            'start_time' TEXT NOT NULL,
            'total_time' INTEGER NOT NULL,
            'max_depth' REAL NOT NULL,
            'location' TEXT,
            'country' TEXT,
            'lat' REAL,
            'lgn' REAL,
            'gas' TEXT,
            'buddy' TEXT,
            'bottom_temp' INTEGER,
            'dive_center' TEXT,
            'boat' TEXT,
            'notes' TEXT
        );
    """
    cur.execute(statement)
    conn.commit()
    print("13. Table 'Dives' created\n")

    # Inserting data
    i = 0
    lat_vals = []
    lgn_vals = []
    text_vals = []
    for dive in dives:
        insertion = (None, 1, dive.num, dive.site, dive.start_date, dive.start_time,
            dive.total_time, dive.max_depth, dive.location, dive.country, dive.lat,
            dive.lgn, dive.gas, dive.buddy, dive.bottom_temp, dive.dive_center,
            dive.boat, dive.notes)
        statement = "INSERT INTO 'Dives' "
        statement += "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(statement, insertion)
        i += 1

        # Lists to create map
        if dive.lat != "":
            lat_vals.append(dive.lat)
            lgn_vals.append(dive.lgn)
            text_vals.append("Dive " + str(dive.num) + ": " + dive.site + "<br />"
                + str(dive.start_date)[:10] + " " + dive.start_time)

    # print(text_vals)
    conn.commit()
    if i == len(dives):
        print("14. Data inserted into table 'Dives' - rows: " + str(i) + " (as expected, woohoo!)\n")
    else:
        print("14. Data inserted into table 'Dives' - rows: " + str(i) + "\n")
    
    conn.close()

    # Plot dives into a map
    fig = go.Figure(data = go.Scattermapbox(
        lat = lat_vals,
        lon = lgn_vals,
        text = text_vals,
        mode = "markers",
        marker_color = "blue",
        )
    )
    layout = dict(
        title = "Divelog Gui Ruggiero",
        autosize = True,
        hovermode = "closest",
        mapbox = dict(
            accesstoken = secret.MAPBOX_TOKEN,
            center = dict(
                lat = mean(lat_vals),
                lon = mean(lgn_vals)
            ),
            zoom = 2,
        )
    )
    fig.update_layout(layout)
    fig.write_html("divelog.html", auto_open = True)

    print("15. Map created\n")
    print("16. That's it for part 2.\n")
    print("17. Final project done. Mission accomplished. Happy holidays!\n")

# Only runs when this file is run directly
if __name__=="__main__":
    import_divelog_csv()
    pass