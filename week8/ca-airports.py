import plotly.graph_objs as go
import csv

f = open('CA-airports.csv')
csv_data = csv.reader(f)

lat_vals = []
lon_vals = []
text_vals = []
for row in csv_data:
    if row[0] != 'iata':
        lat_vals.append(row[5])
        lon_vals.append(row[6])
        text_vals.append(row[0])

min_lat = float(min(lat_vals))
max_lat = float(max(lat_vals))
min_lon = float(min(lon_vals))
max_lon = float(max(lon_vals))
lat_axis = [min_lat - 1, max_lat + 1]
lon_axis = [min_lon - 1, max_lon + 1]
center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2
layout = dict(
        title = 'US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(100, 217, 217)",
            countrycolor = "rgb(217, 100, 217)",
            lataxis = {'range': lat_axis},
            lonaxis = {'range': lon_axis},
            center= {'lat': center_lat, 'lon': center_lon },
            countrywidth = 3,
            subunitwidth = 3
        ),
    )

fig = go.Figure(data=go.Scattergeo(
    lon = lon_vals,
    lat = lat_vals,
    text = text_vals,
    mode = 'markers',
    marker_color = 'red',
    ))

fig.update_layout(layout)

#fig.show()
fig.write_html('CA-airports.html', auto_open=True)