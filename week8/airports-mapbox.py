import plotly.graph_objs as go
import csv
from secret import *

f = open('2011_february_us_airport_traffic.csv')
csv_data = csv.reader(f)

lat_vals = []
lon_vals = []
text_vals = []
for row in csv_data:
    if row[0] != 'iata':
        lat_vals.append(row[5])
        lon_vals.append(row[6])
        text_vals.append(row[0])

layout = dict(
    title = 'US airports on Mapbox<br>(Hover for airport names)',
    autosize=True,
    showlegend = False,
    mapbox=dict(
        accesstoken=MAPBOX_TOKEN,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
      ))

fig = go.Figure(data=go.Scattermapbox(
    lon = lon_vals,
    lat = lat_vals,
    text = text_vals,
    mode = 'markers',
    marker_color = 'red',
    ))

fig.update_layout(layout)

#fig.show()
fig.write_html('airports.html', auto_open=True)