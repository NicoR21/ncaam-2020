import os
import numpy as np
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#Répertoire de sauvegarde des fichiers bruts
DATA_FILES_DIR = '../resources/data/MDataFiles_Stage2/'
PLAY_BY_PLAY_DIR = '../resources/data/MPlayByPlay_Stage2/'

#Table principale
df = 'df_2019.csv'


# Lecture du fichier de données
shot_df = pd.read_csv('df_2019.csv')

# Colors of text and background
colors = {'background': '#FFBB55', 'text': '#2255FF'}

players=[{'label':p, 'value': p} for p in shot_df['FullName'].unique()]


app = dash.Dash('NCAAM_2020')
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='National Collegiate Athletic Association Men 2020 (NCAAM) - Explorer',
        style={'textAlign': 'center', 'color': colors['text']}
    ),

    html.Div(
        children='Players Individual Statistics : 2019-2020',
        style={'textAlign': 'center', 'color': colors['text']}
    ),

    dcc.Tabs([
        dcc.Tab(label='Players shots', children=[
            html.Div([
                dcc.Dropdown(
                    id='player',
                    options=players
                )
            ])
        ])
    ])
])



if __name__ == '__main__':
    app.run_server(debug=True)