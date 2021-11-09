# import dash
# from dash.dependencies import Input, Output
# import dash_core_components as dcc
# import dash_html_components as html
import typing_extensions
from modules import *


############################ Data ########################################
#------------ Data upload
adversaire = pd.read_csv("data/tab_Adversaire.csv")
entraineur= pd.read_csv("data/tab_ClubEntraineur.csv")
clubs = pd.read_csv("data/tab_Clubs.csv")
pays = pd.read_csv("data/tab_Pays.csv")

#------------ Traitement de donnée ---------------------------------------

club_pays = "France"
division = " ligue 2"
nombre_competition= 16
nombre_premierPlace = 1
entraineur= "Roger Mila"



club = "  Feronikeli"
club_logo_link = "https://upload.wikimedia.org/wikipedia/fr/thumb/d/d2/KF_Feronikeli_2.png/800px-KF_Feronikeli_2.png"
nomAdversaire = "The New Saints FC"
df_club_advers = adversaire[(adversaire.NomDesClubs==club) & (adversaire.Nom_Adversaire==nomAdversaire)]


def contenuClub ():

    page_club =  html.Div([ 


        html.Div([

            #  html.Img(src=app.get_asset_url("clubwelcom.jpg"),
            # id='foot-image',
            # style={'height':'60px',
            #         'width':'auto',
            #         'margin-right':'50px'
            #         }),
           html.Div([ 

                html.Img(src=club_logo_link,
                style={'height':'60px',      'width':'auto',      'margin-right':'20px'}),

			    html.B('Club de football de {}'.format(club) ,className='fix_label', style={'color':'#ffb41a',	'fontSize':10}),
               # html.P( club,                   className='fix_label',	style={'color':'#ffb41a',	'fontSize':10}),

           ],className='row flex-display',style={'margin-bottom':'20px'}
           ),


            html.Div([
                
                # club_pays = "France"
                # Division = " ligue 2"
                # Nombre_competition= 16
                # nombre_premierPlace = 1
                # entraineur= "Roger Mila"
                html.Div([ 
                html.P(' PAYS : ',style={'margin-right':'20px','color':'#ffb41a','fontSize':10}),
                html.B(club_pays ,style={'margin-right':'20px','color':'#ffb41a','fontSize':10}), 
                  ],className='row flex-display',style={'margin-bottom':'10px','fontSize':8}),
                
                html.Div([ 
                html.P(' DIVISION : ',style={'margin-right':'20px','color':'#ffb41a','fontSize':10}),
                html.B(division ,style={'margin-right':'20px','color':'#ffb41a'}), 
                  ],className='row flex-display',style={'margin-bottom':'10px','fontSize':8}),

                html.Div([ 
                html.P(' NOMBRE DE COMPETITION : ',style={'margin-right':'10px','color':'#ffb41a'}),
                html.B(division ,style={'margin-right':'20px','color':'#ffb41a'}), 
                  ],className='row flex-display',style={'margin-bottom':'10px','fontSize':8}),

                html.Div([ 
                html.P(' NOMBRE DE PREMIERE PLACE : ',style={'margin-right':'10px','color':'#ffb41a'}),
                html.B(division ,style={'margin-right':'20px','color':'#ffb41a'}), 
                  ],className='row flex-display',style={'margin-bottom':'10px','fontSize':8}),

                html.Div([ 
                html.P(' ENTRAINEUR DU CLUB : ',style={'margin-right':'20px','color':'#ffb41a'}),
                html.B(division ,style={'margin-right':'20px','color':'#ffb41a'}), 
                  ],className='row flex-display',style={'margin-bottom':'10px','fontSize':8}),

              # html.P('Division du club '+ html.B("jhjhjh"),style={'margin-bottom':'20px','color':'#ffb41a'}),
              #  html.P('Nombre de match joué  {} '.format(Nombre_competition)), 
                  


            ])
            
			# html.P('Nouveaux cas:',
			# 	className='fix_label',
			# 	style={'text-align':'center','color':'white'}),

		

		

		],className='create_container three columns'),
			








        html.Div ([


		],className='card_container three columns')
 



        ])
    











    return page_club



            