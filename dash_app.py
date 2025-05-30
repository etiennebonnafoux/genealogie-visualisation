import dash
import plotly.express as px
from dash import dcc, html

from read_data import places_pl

# for deployment, pass app.server (which is the actual flask app) to WSGI etc
app = dash.Dash()


app.layout = html.Div(
    [
        html.H1("Place Locations on World Map"),
        dcc.Graph(
            id="world-map",
            figure=px.scatter_map(
                data_frame=places_pl,
                lat="lat", lon="lon", zoom=3, height=600
            )
            .update_layout(mapbox_style="open-street-map")
            .update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}),
        ),
    ]
)


if __name__ == "__main__":
    app.run()
