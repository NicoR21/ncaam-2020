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
CITIES = "Cities.csv"
CONFERENCES = "Conferences.csv"
MCONFERENCE_TOURNEY_GAMES = "ConferenceTourneyGamesTable.csv"
MGAME_CITIES = "GameCities.csv"
MMASSEY_ORDINALS = "MMasseyOrdinals.csv"
MNCAATOURNEY_COMPACT_RESULTS = "MNCAATourneyCompactResults.csv"
MNCAATOURNEY_DETAILED_RESULTS = "MNCAATourneyDetailedResults.csv"
MNCAATOURNEY_SEED_ROUND_SLOTS = "MNCAATourneySeedRoundSlots.csv"
MNCAATOURNEY_SEEDS = "MNCAATourneySeeds.csv"
MNCAATOURNEY_SLOTS = "MNCAATourneySlots.csv"
MREGULAR_SEASON_COMPACT_RESULTS = "MRegularSeasonCompactResults.csv"
MREGULAR_SEASON_DETAILED_RESULTS = "MRegularSeasonDetailedResults.csv"
MSEASONS = "MSeasons.csv"
MSECONDARY_TOURNEY_COMPACT_RESULTS = "MSecondaryTourneyCompactResults.csv"
MSECONDARY_TOURNEY_TEAMS = "MSecondaryTourneyTeams.csv"
MTEAM_COACHES = "MTeamCoaches.csv"
MTEAM_CONFERENCES = "MTeamConferences.csv"
MTEAMS = "MTeams.csv"
MTEAM_SPELLING = "MTeamSpellings.csv"
EVENTS = "MEvents.csv"
PLAYERS = "MPlayers.csv"


#ENV_FILE='ncaam-2020/env.yaml'
#with open(ENV_FILE) as f:
#    params = yaml.load(f, Loader=yaml.FullLoader)


# Colors of text and background
colors = {'background': '#FFBB55', 'text': '#2255FF'}


app = dash.Dash('NCAAM_2020')
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='National Collegiate Athletic Association Men 2020 (NCAAM) - Explorer',
        style={'textAlign': 'center', 'color': colors['text']}
    ),

    html.Div(
        children='Players Individual Statistics : 2015-2020',
        style={'textAlign': 'center', 'color': colors['text']}
    )
])









if __name__ == '__main__':
    app.run_server(debug=True)