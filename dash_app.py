# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('Processed_daily_sales.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard", id="header"),
    dcc.Dropdown(

        id="region-dropdown",
        options=[{"label": "All Regions", "value": "ALL"}] +
                [{"label": r, "value": r}
                 for r in sorted(df["region"].unique())],
        value="ALL",
        clearable=False
    ),

    dcc.Graph(id="sales-graph")
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):

    if selected_region == "ALL":
        fig = px.line(
            df,
            x="date",
            y="Sales",
            color="region",
            markers=True,
            title="Sales Trend - All Regions"
        )
    else:
        filtered_df = df[df["region"] == selected_region]

        fig = px.line(
            filtered_df,
            x="date",
            y="Sales",
            markers=True,
            title=f"Sales Trend - {selected_region}"
        )

    return fig

if __name__ == "__main__":
    app.run(debug=True)