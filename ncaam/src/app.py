import os
import numpy as np
import yaml
import datetime

import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#Répertoire de sauvegarde des fichiers bruts
DATA_FILES_DIR = '../resources/data/MDataFiles_Stage2/'
PLAY_BY_PLAY_DIR = '../resources/data/MPlayByPlay_Stage2/'

#Tables
CITIES_FILE = "Cities.csv"
CONFERENCES_FILE = "Conferences.csv"
MCONFERENCE_TOURNEY_GAMES_FILE = "ConferenceTourneyGamesTable.csv"
MGAME_CITIES_FILE = "GameCities.csv"
MMASSEY_ORDINALS_TABLE = "MMasseyOrdinals.csv"
MNCAATOURNEY_COMPACT_RESULTS_FILE = "MNCAATourneyCompactResults.csv"
MNCAATOURNEY_DETAILED_RESULTS_FIBLE = "MNCAATourneyDetailedResults.csv"
MNCAATOURNEY_SEED_ROUND_SLOTS_FIBLE = "MNCAATourneySeedRoundSlots.csv"
MNCAATOURNEY_SEEDS_FILE = "MNCAATourneySeeds.csv"
MNCAATOURNEY_SLOTS_FILE = "MNCAATourneySlots.csv"
MREGULAR_SEASON_COMPACT_RESULTS_FILE = "MRegularSeasonCompactResults.csv"
MREGULAR_SEASON_DETAILED_RESULTS_FILE = "MRegularSeasonDetailedResults.csv"
MSEASONS_FILE = "MSeasons.csv"
MSECONDARY_TOURNEY_COMPACT_RESULTS_FILE = "MSecondaryTourneyCompactResults.csv"
MSECONDARY_TOURNEY_TEAMS_FILE = "MSecondaryTourneyTeams.csv"
MTEAM_COACHES_FILE = "MTeamCoaches.csv"
MTEAM_CONFERENCES_FILE = "MTeamConferences.csv"
MTEAMS_FILE = "MTeams.csv"
MTEAM_SPELLING_FILE = "MTeamSpellings.csv"
EVENTS_FILE = "MEvents.csv"
PLAYERS_FILE = "MPlayers.csv"


#ENV_FILE='./env.yaml'
#with open(ENV_FILE) as f:
#    params = yaml.load(f, Loader=yaml.FullLoader)

# Colors of text and background
colors = {
    'background': '#FFBB55',
    'text': '#2255FF'
}

app = dash.Dash('')
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='National Collegiate Athletic Aassociation Men 2020 (NCAAM) - Explorer',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Players Individual Statistics : 2015-2020', style={
        'textAlign': 'center',
        'color': colors['text']
    })
])








if __name__ == '__main__':
    app.run_server(debug=True)