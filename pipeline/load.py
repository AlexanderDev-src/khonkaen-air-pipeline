import sqlite3

import pandas as pd

from pipeline.config import DATA_BASE_LOCATION


def dataframe_to_sql(df: pd.DataFrame) -> pd.DataFrame:
    connect = sqlite3.connect(DATA_BASE_LOCATION)
    df.to_sql("data", connect, if_exists="replace", index=False)
    data = pd.read_sql("SELECT * FROM data", connect, parse_dates="time")
    connect.close()
    return data
