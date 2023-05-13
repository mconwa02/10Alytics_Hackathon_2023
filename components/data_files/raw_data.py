import pandas as pd
import os

from components.config import DATA_DIR
from components.data_files.data_config import EXCEL_FILE_NAMES


def read_excel_files():
    for file_name in EXCEL_FILE_NAMES:
        file = file_name + ".xlsx"
        df = pd.read_excel(os.path.join(DATA_DIR, file))
        print(file_name, df.head())
        print(df.describe())

def read_csv_files():
    for file_name in EXCEL_FILE_NAMES:
        file = file_name + ".csv"
        df = pd.read_csv(os.path.join(DATA_DIR, file))
        print(file_name, df.head())
        print(df.describe())


if __name__ == "__main__":
    read_excel_files()
    read_csv_files()
