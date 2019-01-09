#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# create a DataFrame from the .csv file:
df = pd.read_csv('mpg.csv')
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']

# create data by choosing fields for x, y and marker size attributes
data= [go.Scatter(
            x=df['acceleration'],
            y=df['mpg'],
            text=df['text2'],
            mode='markers',
            marker=dict(size=df['weight']/100,
                       color=df['cylinders'],
                       showscale=True))]

# create a layout with a title and axis labels
layout = go.Layout(title='Vehicle mpg vs. Acceleration',hovermode='closest')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')
