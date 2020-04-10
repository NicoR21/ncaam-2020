from pathlib import Path

import pandas as pd

from ncaam.src.constants import DATA_PATH, DATA_FILES, PLAY_BY_PLAY, STAGE, \
    EVENTS_TABLE, PLAYERS_TABLE, CITIES_TABLE, CONFERENCES_TABLE


class Loader:  # Nom de classe separe par une majuscule
    def __init__(self, local: bool = True) -> None:
        self.local = local

    def import_data(self, desired_tables: list = ["events", "players", "cities"]) -> (pd.DataFrame, pd.DataFrame):
        data = {}
        if self.local:
            if "events" in desired_tables:
                data["events"] = self._import_events()
            if "players" in desired_tables:
                data["players"] = self._import_players()
            if "cities" in desired_tables:
                data["cities"] = self._import_data_file(CITIES_TABLE)
            if "conferences" in desired_tables:
                data["conferences"] = self._import_data_file(CONFERENCES_TABLE)

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

    def _import_data_file(self, table_name: str) -> pd.DataFrame:
        if self.local:
            data_path = self._get_loading_path()
            return pd.read_csv(f"{data_path}/{DATA_FILES}_{STAGE}2/{table_name}.csv")

    @staticmethod
    def _get_loading_path() -> str:
        return f"{Path(__file__).parents[3]}/{DATA_PATH}"
