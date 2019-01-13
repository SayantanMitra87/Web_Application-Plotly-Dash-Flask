import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

app.layout = html.Div([ # Dash infrastructure
    dcc.Graph(          # Dash infrastructure
        id='scatter3',  # Dash infrastructure # id might help to reference it back
        figure={        # Dash infrastructure
            'data': [   # Dash infrastructure
                go.Scatter( # from here what we have done to plot a plotly interactive graph
                    x = random_x,       # Plotly code
                    y = random_y,       # Plotly code
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
                title = 'Random Data Scatterplot',          # Plotly code
                xaxis = {'title': 'Some random x-values'},  # Plotly code
                yaxis = {'title': 'Some random y-values'},  # Plotly code
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':  # Dash infrastructure
    app.run_server()        # Dash infrastructure
