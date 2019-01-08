import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('nst-est2017-alldata.csv')
(df.head())

filt = df['DIVISION']=='1'
df2 = df[filt]
df2.set_index('NAME', inplace=True)
print(df2.head())

cols = [col for col in df.columns if col.startswith('POP')]
df2 = df2[cols]

data = [go.Scatter(x=df2.columns,
                   y=df2.loc[name],
                   mode='lines',
                   name=name) for name in df2.index]

pyo.plot(data)
