import pandas as pd
from ncaam.src.constants import DATA_PATH


class Loader:  # Nom de classe separe par une majuscule
    def __init__(self, local: bool = True) -> None:
        self.local = local

    def import_data(self, table_name: str) -> tuple:
        if self.local:
            return pd.read_csv(f"{DATA_PATH}/MDataFiles_Stage1/{table_name}.csv"), \
                   pd.read_csv(f"{DATA_PATH}/MDataFiles_Stage2/{table_name}.csv")
