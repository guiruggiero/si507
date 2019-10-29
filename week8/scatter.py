import numpy as np
import plotly.graph_objs as go

# Create random data with numpy
N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)
data = [trace]
fig = go.Figure(data=data)
fig.write_html('scatter.html', auto_open=True)
#fig.show()