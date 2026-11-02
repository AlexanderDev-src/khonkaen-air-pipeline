import pandas as pd


def weather_data_transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df


def air_data_transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df
