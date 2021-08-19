import pandas as pd

import plotly.express as pe

df = pd.read_csv("data.csv")
fig = pe.scatter(df, x="date", y="cases", color="country")
fig.show()