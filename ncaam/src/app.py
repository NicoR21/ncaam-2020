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
PLAY_BY_PLAY_DIR = '../resources/data/MPlayByPlay_Stage2'

ENV_FILE='./env.yaml'
with open(ENV_FILE) as f:
    params = yaml.load(f, Loader=yaml.FullLoader)