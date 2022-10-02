from __future__ import annotations
# from airflow.models import Variable
from airflow.decorators import task
import requests
import json

# API_KEY = Variable.get('OPEN_WEATHER_API_KEY')
API_KEY = "f0f0f3b9c1ee0f12af4f07cdacf02468"

@task()
def extract():
    paramaters = {'q': 'Jakarta, ID', 'appid': API_KEY}
    result = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?", paramaters)
    
    if result.status_code == 200:
        # Get the json data
        weather_data_dict = dict(result.json())
        
        return weather_data_dict
