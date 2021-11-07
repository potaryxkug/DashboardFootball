

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
#from Dashboard.pages.club import contenuClub

from pages.club import *




############################ Data ########################################
#------------ Data upload
adversaire = pd.read_csv("data/tab_Adversaire.csv")
entraineur= pd.read_csv("data/tab_ClubEntraineur.csv")
clubs = pd.read_csv("data/tab_Clubs.csv")
pays = pd.read_csv("data/tab_Pays.csv")

#------------ 


#-------------Début
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


########################## Styl css #####################################
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}



########################### Layout #######################################

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Les joueurs', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Les clubs', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Equipe Nationale ', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Autres info football', value='tab-4', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])

 

########################## Caallback #######################################


@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Les joueurs'),

            html.H1('Welcome to the website!'),
            html.H2('Text',
            style={'font-size':'50px',
            'color':'red'},)





        ])
    elif tab == 'tab-2':
        return contenuClub()
        
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4')
        ])

# def callback_a(x):
#     return x**2, x**3, 2**x, 3**x, x**x




if __name__ == '__main__':
    app.run_server(debug=True)
