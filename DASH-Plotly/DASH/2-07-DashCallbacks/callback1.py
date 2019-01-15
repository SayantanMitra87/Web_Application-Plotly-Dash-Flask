import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'), # dcc.input() is a part of core component. Code taken from website
    html.Div(id='my-div') # This will create a spacce. To see that we can pass a style `style={'border': '2px blue solid'}`
])

# Now dash core component (dcc.input) and html component(html.div) can be connected by callback
@app.callback(
    Output(component_id='my-div', component_property='children'), # we want the output to the in html.div whose id is 'my-div'
    [Input(component_id='my-id', component_property='value')] # value selected from the dcc.input (deafult was 'initialvalue' and that would be displayed)
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()
