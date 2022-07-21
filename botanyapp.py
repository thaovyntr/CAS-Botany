import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

#load data into pandas
df = pd.read_csv(r'/Users/a1/Downloads/PortalFiles/PortalData.csv', 
                 usecols=["latitude1","longitude1","fullName",
                          "Class","Order","Family","Species",
                          "Continent","Country"])

#creating map
fig = px.scatter_geo(df,
                     projection = 'orthographic',
                     lat='latitude1',
                     lon='longitude1', 
                     hover_name="fullName", 
                     color='Continent',
                     hover_data=['Class',
                                 'Order',
                                 'Family',
                                 'Species',
                                 'Country'])
fig.update_layout(title = 'Map of plant species around the world', title_x=0.5)
fig.show()

#Dash layout
app.layout = html.Div(children=[
    html.H1(children='Map of plant species around the world'),
    html.Div(children='This data was provided by California Academy of Science.'),

    dcc.Graph(
        id='botany-map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)