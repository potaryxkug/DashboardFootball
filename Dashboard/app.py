

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

#style={'width':'500px', 'height':'450px', 'border':'5px dotted red'}
########################## Styl css #####################################
tabs_styles = {
    'height': '30px', 'width':'1050px', "margin": "0 auto",'color': 'blue', #'border': '1px solid #d6d6d6' ,
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'border-radius':'15px',
    'background-color':'#F2F2F2',
    'box-shadow':'4px 4px 4px lightgrey'
    
}

tab_selected_style = {
   # 'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#172763',
    'color': 'white',
    'padding': '6px',
    'border-radius':'15px'
}


##119DFF





########################### Layout #######################################

app.layout = html.Div([

        	# -----------Objet 1 image ---------
		    html.Div([
			

        html.Img(src=app.get_asset_url("clubwelcom.jpg"),
            id='foot-image',
            style={'height':'80px',
                    'width':'auto',
                    'margin-right':'50px',
                    'margin-bottom':'30px'
                    }),

        html.H3(' Football_data_VISUALIZATION  ', style={'margin-bottom':'30px','color':'white','width':'auto','margin-right':'50px'}
        ),


         html.Img(src=app.get_asset_url("soccer.jpg"),
            id='foot-image1',
            style={'height':'80px',
                    'width':'auto',
                    'margin-right':'50px',
                    'margin-bottom':'30px'
                    }),
      
       			
		],id='header',className='row flex-display',style={ 'width':'20px','height':'15px','margin-bottom':'30px',
            #'margin': '10px auto'
        }),

        
   
     
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
