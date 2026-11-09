from pathlib import Path

CONFIG_FILE = Path(__file__).resolve()
APP_DIR = CONFIG_FILE.parent
PROJECT_DIR = CONFIG_FILE.parent.parent
DATA_PATH = PROJECT_DIR / "data"
DATA_PATH_RAW = DATA_PATH / "raw"
DATA_PATH_WAREHOUSE = DATA_PATH / "warehouse"
DATA_BASE_LOCATION = DATA_PATH_WAREHOUSE / "data.db"


LATITUDE = 16.44
LONGITUDE = 102.84
TIME_ZONE = "Asia/Bangkok"
# ----
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS_METEO = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "hourly": [
        "relative_humidity_2m",
        "temperature_2m",
        "is_day",
        "rain",
        "wind_speed_10m",
        "wind_direction_10m",
    ],
    "timezone": TIME_ZONE,
}
# ----
AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
PARAMS_AIR_QUALITY = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "hourly": ["pm10", "pm2_5"],
    "timezone": TIME_ZONE,
}
