# SI 507 - final project, part 2
# Developed by Gui Ruggiero

import classes
import csv
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

    # Extracting data and building instances
    for row in csv_data:
        if row[0] != 'iata':
            lat_vals.append(row[5])
            lon_vals.append(row[6])
            text_vals.append(row[0])

#import_divelog_csv()