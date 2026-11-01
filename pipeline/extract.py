import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

from pipeline.config import (
    AIR_QUALITY_URL,
    DATA_PATH_RAW,
    OPEN_METEO_URL,
    PARAMS_AIR_QUALITY,
    PARAMS_METEO,
    TIME_ZONE,
)

# --- Time zone format ---
TIME_ZONE_INFO = ZoneInfo(TIME_ZONE)
# ---


def fetch_and_save_json(url: str, params: dict, output_path: Path) -> dict:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return data


def get_meteo_data() -> dict:
    date = format_time_zone()

    return fetch_and_save_json(
        OPEN_METEO_URL,
        PARAMS_METEO,
        DATA_PATH_RAW / f"weather_data_{date}.json",
    )


def get_air_data() -> dict:
    date = format_time_zone()

    return fetch_and_save_json(
        AIR_QUALITY_URL,
        PARAMS_AIR_QUALITY,
        DATA_PATH_RAW / f"air_data_{date}.json",
    )


def format_time_zone() -> str:
    return datetime.now(TIME_ZONE_INFO).strftime("%Y-%m-%d")
