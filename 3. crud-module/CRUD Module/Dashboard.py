"""
Module Name: Dashboard.py
Description: This program builds a dataframe-based dashboard by
accessing a database through the CRUD functionality of Module.py.
Author: Sebastian Stohn
Date: 2026-08-03
"""

from dash import Dash, dcc, html, dash_table, Input, Output, State, ctx
import dash_leaflet as dl
import plotly.express as px
import pandas as pd
import base64

from Module import NationalParkDatabase

username = 'SebStohn'
password = 'Password2026'
parks = NationalParkDatabase(username, password)

# Reads from the database using the Module
df = pd.DataFrame.from_records(parks.read({}))
df.drop(columns = ['_id'], inplace = True)

# Adjust 'visited' and 'website' fields to be more useful
df["visited"] = df["visited"].map({True: "Yes", False: "No"})
df['website'] = df['website'].apply(lambda x: f'[Link]({x})')

# Dropdown menu
states = sorted(df['state'].dropna().unique())

app = Dash(__name__)

# Corner image
image_filename = 'icon.jpg'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# Displayed columns
columns = [
    'name',
    'state',
    'visited',
    'acres',
    'latitude',
    'longitude',
    'year_open',
    'website'
]


# Dashboard layout
app.layout = html.Div([
    html.Div([
        html.Img(
            src = 'data:image/png;base64,{}'.format(encoded_image.decode()),
            style = {'width': '64px'}
        ),
        html.B(html.H1('National Parks Database'))
    ],
        style = {
            'display': 'flex',
            'alignItems': 'center',
            'color': '#1b1a18'
        }
    ),
    html.Hr(),

    # Dropdown menu layout
    html.Div([
        dcc.Dropdown(
            id = 'state-filter',
            options = [{'label': 'All States', 'value': 'ALL'}] +
                      [{'label': state, 'value': state} for state in states],
            value = 'ALL',
            clearable = False,
            style = {
                'width': '15%',
                'minWidth': '150px',
                'maxWidth': '300px'
            }
        ),

        # Update button
        html.Button(
            'Update Visited',
            id = 'update-visited',
            n_clicks = 0
        )
    ],
        style = {
            'display': 'flex',
            'alignItems': 'center',
            'gap': '8px'
        }
    ),
    html.Hr(),

    # Main table layout
    dash_table.DataTable(
        id = 'datatable-id',
        columns = [{
            'name': i,
            'id': i,
            'deletable': False,
            'presentation': 'markdown' if i == 'website' else 'input'
        } for i in columns],
        data = df.to_dict('records'),
        row_selectable = 'single',
        sort_action = 'native',
        page_action = 'native',
        page_size = 9,
        markdown_options = {'html': True},
        style_header = {
            'backgroundColor': '#1b1a18',
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_cell = {'textAlign': 'center'},
    ),
    html.Hr(),

    # Holds pie graph and geolocation map
    html.Div(
        className = 'row',
        style = {'display': 'flex', 'flexWrap': 'wrap'},
        children = [

            # Pie graph
            html.Div(
                id = 'graph-id',
                style = {"flex": '1', "minWidth": '240px'},
            ),

            # Geolocation map
            html.Div(
                id = 'map-id',
                style = {'flex': '1', 'minWidth': '240px'},
            )
        ]
    )
])


# Callback to populate the dataframe
@app.callback(
    Output('datatable-id', 'data'),
    Input('state-filter', 'value'),
    Input('update-visited', 'n_clicks'),
    State('datatable-id', 'derived_virtual_data'),
    State('datatable-id', 'derived_virtual_selected_rows')
)


def update_dashboard(selected_state, _, rows, selected):
    """ Updates dashboard by reading database through CRUD Module """
    # Update 'visited' field triggered by button
    if ctx.triggered_id == 'update-visited':
        if selected and rows:
            dff = pd.DataFrame(rows)
            row = selected[0]
            park = dff.iloc[row]
            current_status = park['visited']

            parks.update(
                {'name': park['name']},
                {'$set': {'visited': current_status != 'Yes'}}
            )

    # Read database based on dropdown menu
    if selected_state == 'ALL':
        query = {}
    else:
        query = {'state': selected_state}

    # Read database to populate dataframe
    dff = pd.DataFrame.from_records(parks.read(query))

    # Adjust 'visited' field to be more useful
    dff["visited"] = dff["visited"].map({True: "Yes", False: "No"})

    if '_id' in dff.columns:
        dff.drop(columns = ['_id'], inplace = True)

    # Adjust 'website' field to be more useful
    if 'website' in dff.columns:
        dff['website'] = dff['website'].apply(lambda x: f'[Link]({x})')

    return dff.to_dict('records')


# Callback to update the pie graph
@app.callback(
    Output('graph-id', 'children'),
    Input('datatable-id', 'derived_virtual_data')
)


def update_graphs(view_data):
    """ Updates pie graph based on dataframe """
    if view_data is None:
        return

    dff = pd.DataFrame.from_dict(view_data)

    # Return graph with number of parks in each state
    return [dcc.Graph(
        figure = px.pie(
            dff,
            title = 'Number of Parks by State',
            names = 'state',
            hole = 0.3,

            # 33 color gradient for each territory with a park
            color_discrete_sequence = [
                '#f4cd82', '#f2c66f', '#f0bf5d', '#eeb84b', '#ecb13b', '#eaa92d',
                '#e7a124', '#f8951e', '#ef8a1b', '#e67e18', '#dc7317', '#d16816',
                '#c65d16', '#ba5217', '#ae4818', '#a13e19', '#94351a', '#872e1a',
                '#7a281a', '#6d241a', '#60211a', '#54201a', '#48201a', '#3d201b',
                '#35201b', '#2f201b', '#29201b', '#25201b', '#211e1a', '#1f1d19',
                '#1d1b18', '#1c1a18', '#1b1a18'
            ]
        ).update_traces(textinfo='value'),
        responsive = True,
        style = {'width': '100%', 'height': '60vh'}
    )]


# Callback to update the geolocation map
@app.callback(
    Output('map-id', 'children'),
    Input('datatable-id', 'derived_virtual_data'),
    Input('datatable-id', 'derived_virtual_selected_rows')
)


def update_map(view_data, index):
    """ Updates geolocation map based on selected park """
    if view_data is None:
        return
    elif index is None:
        return

    dff = pd.DataFrame.from_dict(view_data)

    if not index:
        return
    else:
        row = index[0]

    # Define geolocation based on dataframe
    lat = dff.iloc[row]['latitude']
    lon = dff.iloc[row]['longitude']

    # Return map centered around park
    return [
        dl.Map(
            style = {'width': '100%', 'height': '60vh'},
            center = [lat, lon],
            zoom = 6,
            children = [
                dl.TileLayer(id = 'base-layer-id'),
                dl.Marker(
                    position = [lat, lon],
                    children = [

                        # Shows lat and lon when hovered
                        dl.Tooltip(
                            f"{dff.iloc[row]['latitude']}, "
                            f"{dff.iloc[row]['longitude']}"),

                        # Shows name and state when clicked
                        dl.Popup([
                            html.H3(dff.iloc[row]['name']),
                            html.P(dff.iloc[row]['state'])
                        ])
                    ]
                )
            ]
        )
    ]


# Run app
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8050)