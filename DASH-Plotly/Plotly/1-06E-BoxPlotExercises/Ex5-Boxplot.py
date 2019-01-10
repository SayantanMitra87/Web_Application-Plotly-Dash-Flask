#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('abalone.csv')

# take two random samples of different sizes:
np.random.seed(101)
abc = np.random.choice(df['rings'], 30, replace=False)
xyz = np.random.choice(df['rings'], 20, replace=False)

# create a data variable with two Box plots:
data = [go.Box(y=abc, name='abc'),
        go.Box(y=xyz, name='xyz')]

# add a layout
layout = go.Layout(title = 'abc vs xyz')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box3.html')
