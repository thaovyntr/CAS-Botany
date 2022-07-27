import dash
from dash import dcc
from dash import html
from dash import Input, Output
import plotly.express as px
import pandas as pd
import json
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)


#load data into pandas
df = pd.read_csv(r'/Users/a1/Downloads/PortalFiles/PortalData.csv', 
                 usecols=["latitude1","longitude1","fullName",
                          "Class","Order","Family","Species",
                          "Continent","Country"])

#create map
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
#fig.update_layout(title = 'Map of plant species around the world', title_x=0.5)
fig.show()



#Dash layout
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div(
    children=[
        html.H1(children='Map of plant species around the world'),

        html.Span("Hover over a plant on the map to see its information."),
        html.Br(),

        dcc.Graph(
            id='botany-map',
            figure=fig
        ),


        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
                """),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),
    ]

)               

@app.callback(
    Output('click-data', 'children'),
    Input('botany-map', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)   



if __name__ == '__main__':
    app.run_server(debug=True)