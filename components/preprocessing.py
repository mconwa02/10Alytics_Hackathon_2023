import pandas as pd

from components.data_files.data_config import COUNTRY_CODE


def format_columns(df):
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
    return df


def create_transposed_life_expectancy_data(df):
    df = df.set_index("year")
    transposed_df = pd.DataFrame()
    for col in COUNTRY_CODE:
        transposed_df[col] = df[["life_expectancy_at_birth_(historical)"]][
            df.code == col
        ]
    return transposed_df
