from time import sleep

from pipeline.extract import get_air_data, get_meteo_data
from pipeline.load import dataframe_to_sql
from pipeline.transform import air_data_transform, merge_data, weather_data_transform

print("Extracting Air Data....")
try:
    air_data = get_air_data()
    print("Getting Data Completed")
except Exception as ex:
    print("Can't extract data")
    print(ex)
    raise

print("Extracting Weather Data....")
try:
    weather_data = get_meteo_data()
    print("Getting Data Completed")
except Exception as ex:
    print("Can't extract data")
    print(ex)
    raise

print("Finish Extracting Data... Next Transformation")
sleep(2)

print("\n------ Transforming ------")
try:
    print("Weather data transforming")
    weather_trans = weather_data_transform(weather_data)
    try:
        print("Air data transformation")
        air_trans = air_data_transform(air_data)
    except Exception as ex:
        print(ex)
        raise
except Exception as ex:
    print(ex)
    raise
finally:
    print("Finish transform")


print("Extracting Data [Done], Transformation [Done], Next is Merging")
sleep(2)

print("\n----- Merging -----")
try:
    merged_data = merge_data(air_data=air_trans, weather_data=weather_trans)
except Exception as ex:
    print(ex)
    raise
finally:
    print("Merged Done")

print("\n---- Loading Data -----")
sleep(2)

try:
    dataframe_to_sql(df=merged_data)
except Exception as ex:
    print(ex)
    raise
finally:
    print("Loading Done! Check */data/?")


print("\n\n ----- Finish process")
