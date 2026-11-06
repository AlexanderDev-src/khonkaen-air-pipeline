import pandas as pd


def weather_data_transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df


def air_data_transform(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    return df


def merge_data(air_data: pd.DataFrame, weather_data: pd.DataFrame) -> pd.DataFrame:
    air_weather_merge = weather_data.merge(air_data, on="time", how="inner")
    return air_weather_merge
