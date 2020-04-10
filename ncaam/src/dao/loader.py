import pandas as pd
from ncaam.src.constants import DATA_PATH, DATA_FILES, PLAY_BY_PLAY, STAGE


class Loader:  # Nom de classe separe par une majuscule
    def __init__(self, local: bool = True) -> None:
        self.local = local

    def import_data_files(self, table_name: str) -> (pd.DataFrame, pd.DataFrame):
        if self.local:
            return pd.read_csv(f"{DATA_PATH}/{DATA_FILES}_{STAGE}1/{table_name}.csv"), \
                   pd.read_csv(f"{DATA_PATH}/{DATA_FILES}_{STAGE}2/{table_name}.csv")

    def import_play_by_play(self, table_name: str) -> (pd.DataFrame, pd.DataFrame):
        if self.local:
            return pd.read_csv(f"{DATA_PATH}/{PLAY_BY_PLAY}_{STAGE}1/{table_name}.csv"), \
                   pd.read_csv(f"{DATA_PATH}/{PLAY_BY_PLAY}_{STAGE}2/{table_name}.csv")
