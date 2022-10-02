from __future__ import annotations
from airflow.decorators import task

@task()
def transform(weather_data_dict: dict, **kwargs):
    city = str(weather_data_dict['name'])
    country = str(weather_data_dict['sys']['country'])
    lat = float(weather_data_dict['coord']['lat'])
    lon = float(weather_data_dict['coord']['lon'])
    humid = float(weather_data_dict['main']['humidity'])
    press = float(weather_data_dict['main']['pressure'])
    min_temp = float(weather_data_dict['main']['temp_min']) - 273.15
    max_temp = float(weather_data_dict['main']['temp_max']) - 273.15
    temp = float(weather_data_dict['main']['temp']) - 273.15
    weather = str(weather_data_dict['weather'][0]['description'])
    todays_date = str(kwargs["execution_date"]).split('T')[0]

    transform_res = {city, country, lat, lon, humid, press, min_temp, max_temp, temp, weather, todays_date}

    return list(transform_res)