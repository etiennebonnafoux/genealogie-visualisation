import dash
import plotly.express as px
import polars as pl
from dash import dcc, html

from read_data import df_place
from utils import dms_to_dd

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()

print(df_place.columns)

df_place = df_place.with_columns(
    pl.col("lat").map_elements(dms_to_dd, return_dtype=pl.Float32).alias("latitude")
)
df_place = df_place.with_columns(
    pl.col("long").map_elements(dms_to_dd, return_dtype=pl.Float32).alias("longitude")
)
print(df_place.columns)

app.layout = html.Div(
    [
        html.H1("Place Locations on World Map"),
        dcc.Graph(
            id="world-map",
            figure=px.scatter_map(
                df_place, lat="latitude", lon="longitude", zoom=3, height=600
            )
            .update_layout(mapbox_style="open-street-map")
            .update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}),
        ),
    ]
)


if __name__ == "__main__":
    app.run()
