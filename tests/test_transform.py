import pandas as pd

from pipeline.transform import air_data_transform, merge_data, weather_data_transform


def test_weather_data_transform():
    fake = {
        "hourly": {
            "time": [
                "2026-11-09T00:00",
                "2026-11-09T01:00",
                "2026-11-09T02:00",
                "2026-11-09T03:00",
            ],
            "relative_humidity_2m": [
                71,
                75,
                77,
                78,
            ],
            "temperature_2m": [
                26.5,
                25.4,
                24.9,
                24.5,
            ],
            "is_day": [
                0,
                0,
                1,
                1,
            ],
            "rain": [
                0.0,
                0.0,
                0.1,
                0.1,
            ],
            "wind_speed_10m": [
                16.7,
                15.5,
                14.8,
                13.6,
            ],
            "wind_direction_10m": [
                73,
                75,
                72,
                64,
            ],
        }
    }
    result = weather_data_transform(fake)
    assert len(result) == 4
    assert list(result.columns) == [
        "time",
        "relative_humidity_2m",
        "temperature_2m",
        "is_day",
        "rain",
        "wind_speed_10m",
        "wind_direction_10m",
    ]
    assert all(0 <= value <= 1 for value in result["is_day"])
    assert pd.api.types.is_datetime64_any_dtype(result["time"])


def test_air_data_transform():
    fake = {
        "hourly": {
            "time": [
                "2026-11-09T00:00",
                "2026-11-09T01:00",
                "2026-11-09T04:00",
                "2026-11-09T05:00",
            ],
            "pm10": [
                5.2,
                4.6,
                15.9,
                26.1,
            ],
            "pm2_5": [
                10.2,
                3.4,
                6.0,
                25.4,
            ],
        }
    }
    result = air_data_transform(fake)
    assert len(result) == 4
    assert list(result.columns) == [
        "time",
        "pm10",
        "pm2_5",
    ]
    assert pd.api.types.is_datetime64_any_dtype(result["time"])


def test_merge_data():
    fake_weather = {
        "time": [
            "2026-11-09T00:00",
            "2026-11-09T01:00",
            "2026-11-09T02:00",
            "2026-11-09T03:00",
        ],
        "relative_humidity_2m": [
            71,
            75,
            77,
            78,
        ],
        "temperature_2m": [
            26.5,
            25.4,
            24.9,
            24.5,
        ],
        "is_day": [
            0,
            0,
            1,
            1,
        ],
        "rain": [
            0.0,
            0.0,
            0.1,
            0.1,
        ],
        "wind_speed_10m": [
            16.7,
            15.5,
            14.8,
            13.6,
        ],
        "wind_direction_10m": [
            73,
            75,
            72,
            64,
        ],
    }
    fake_air = {
        "time": [
            "2026-11-09T00:00",
            "2026-11-09T01:00",
            "2026-11-09T05:00",
            "2026-11-09T07:00",
        ],
        "pm10": [
            5.2,
            4.6,
            15.9,
            26.1,
        ],
        "pm2_5": [
            10.2,
            3.4,
            6.0,
            25.4,
        ],
    }
    fake_air_df = pd.DataFrame(fake_air)
    fake_weather_df = pd.DataFrame(fake_weather)
    result = merge_data(air_data=fake_air_df, weather_data=fake_weather_df)
    assert len(result) == 2
    assert list(result.columns) == [
        "time",
        "relative_humidity_2m",
        "temperature_2m",
        "is_day",
        "rain",
        "wind_speed_10m",
        "wind_direction_10m",
        "pm10",
        "pm2_5",
    ]
    assert len(result.columns) == 9
