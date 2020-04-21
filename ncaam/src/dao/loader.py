import glob
from pathlib import Path

import pandas as pd

from ncaam.src.constants import DATA_PATH, DATA_FILES, PLAY_BY_PLAY, STAGE, \
    CITIES_TABLE, CONFERENCES_TABLE, MCONFERENCE_TOURNEY_GAMES_TABLE, MGAME_CITIES_TABLE, MMASSEY_ORDINALS_TABLE, \
    MNCAATOURNEY_COMPACT_RESULTS_TABLE, MNCAATOURNEY_DETAILED_RESULTS_TABLE, MNCAATOURNEY_SEED_ROUND_SLOTS_TABLE, \
    MNCAATOURNEY_SEEDS_TABLE, MNCAATOURNEY_SLOTS_TABLE, MREGULAR_SEASON_COMPACT_RESULTS_TABLE, \
    MREGULAR_SEASON_DETAILED_RESULTS_TABLE, MSEASONS_TABLE, MSECONDARY_TOURNEY_COMPACT_RESULTS_TABLE, \
    MSECONDARY_TOURNEY_TEAMS_TABLE, MTEAM_COACHES_TABLE, MTEAM_CONFERENCES_TABLE, MTEAMS_TABLE, \
    MTEAM_SPELLING_TABLE, EVENTS_TABLE, PLAYERS_TABLE

DESIRED_TABLES: list = [CITIES_TABLE, CONFERENCES_TABLE, MCONFERENCE_TOURNEY_GAMES_TABLE, MGAME_CITIES_TABLE,
                        MMASSEY_ORDINALS_TABLE, MNCAATOURNEY_COMPACT_RESULTS_TABLE,
                        MNCAATOURNEY_DETAILED_RESULTS_TABLE, MNCAATOURNEY_SEED_ROUND_SLOTS_TABLE,
                        MNCAATOURNEY_SEEDS_TABLE, MNCAATOURNEY_SLOTS_TABLE,
                        MREGULAR_SEASON_COMPACT_RESULTS_TABLE, MREGULAR_SEASON_DETAILED_RESULTS_TABLE,
                        MSEASONS_TABLE, MSECONDARY_TOURNEY_COMPACT_RESULTS_TABLE, MSECONDARY_TOURNEY_TEAMS_TABLE,
                        MTEAM_COACHES_TABLE, MTEAM_CONFERENCES_TABLE, MTEAMS_TABLE, MTEAM_SPELLING_TABLE,
                        EVENTS_TABLE, PLAYERS_TABLE]


class Loader:  # Nom de classe separe par une majuscule
    def __init__(self, local: bool = True) -> None:
        self.local = local

    def import_data(self, desired_tables: list = DESIRED_TABLES) -> dict:
        data = {}
        if self.local:
            data_files_tables = [table for table in desired_tables if table not in [EVENTS_TABLE, PLAYERS_TABLE]]
            if EVENTS_TABLE in desired_tables:
                data[EVENTS_TABLE] = self._import_events()
            if PLAYERS_TABLE in desired_tables:
                data[PLAYERS_TABLE] = self._import_players()
            if data_files_tables:
                data_files = self._import_data_file(data_files_tables)
                data.update(data_files)

        return data

    def _import_events(self) -> pd.DataFrame:
        if self.local:
            data_path = self._get_loading_path()
            events_df = pd.DataFrame()
            for y in range(2015, 2021):
                df = pd.read_csv(f"{data_path}/{PLAY_BY_PLAY}_{STAGE}2/{EVENTS_TABLE}{y}.csv")
                events_df = pd.concat([events_df, df], ignore_index=True)
        else:
            pass

        return events_df

    def _import_players(self) -> pd.DataFrame:
        if self.local:
            data_path = self._get_loading_path()
            return pd.read_csv(f"{data_path}/{PLAY_BY_PLAY}_{STAGE}2/{PLAYERS_TABLE}.csv")

    def _import_data_file(self, data_files_tables: list) -> dict:
        data_files = {}

        if self.local:
            data_path = self._get_loading_path()
            all_data_files_tables = glob.glob(f"{data_path}/{DATA_FILES}_{STAGE}2/*.csv")
            desired_data_files_tables = [table for table in all_data_files_tables if
                                         table.split("/")[-1].split(".csv")[0] in data_files_tables]
            for table in desired_data_files_tables:
                table_name = table.split("/")[-1].split(".csv")[0]
                data_files[table_name] = pd.read_csv(table)
        else:
            pass

        return data_files

    @staticmethod
    def _get_loading_path() -> str:
        return f"{Path(__file__).parents[3]}/{DATA_PATH}"
