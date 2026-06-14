# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('Processed_daily_sales.csv')

fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Daily Sales Trend",
    markers=True
)
app.layout = html.Div(children=[
    html.Div(children='''
        Dash: A web application framework for line graph.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)