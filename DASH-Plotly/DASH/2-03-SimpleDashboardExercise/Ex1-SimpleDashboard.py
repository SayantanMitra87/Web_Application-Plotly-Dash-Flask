#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
df = pd.read_csv('OldFaithful.csv')
x = df['X']
y = df['Y']

# Create a Dash layout that contains a Graph component:
app.layout = html.Div([ # Dash infrastructure
    dcc.Graph(          # Dash infrastructure
        id='scatter',  # Dash infrastructure # id might help to reference it back
        figure={        # Dash infrastructure
            'data': [   # Dash infrastructure
                go.Scatter( # from here what we have done to plot a plotly interactive graph
                    x = x,       # Plotly code
                    y = y,       # Plotly code
                    mode = 'markers',   # Plotly code
                    marker = {          # Plotly code
                        'size': 12,     # Plotly code
                        'color': 'rgb(51,204,153)',     # Plotly code
                        'symbol': 'pentagon',           # Plotly code
                        'line': {'width': 2}            # Plotly code
                        }
                )
            ],
            'layout': go.Layout( # How we do layout for plotly
                title = 'Old Faithful',          # Plotly code
                xaxis = {'title': 'duration of the current eruption in mins (to nearest 0.1 min)'},  # Plotly code
                yaxis = {'title': 'waiting time until next eruption in mins (to nearest min)'},  # Plotly code
                hovermode='closest'
            )
        }
    )
])
# Add the server clause:
if __name__ == '__main__':  # Dash infrastructure
    app.run_server()        # Dash infrastructure
