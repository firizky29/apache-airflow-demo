from __future__ import annotations
import pendulum
from airflow.decorators import dag, task
from etl.extract import extract
from etl.transform import transform
from etl.load import load


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=['demo-etl'],
)
def weather_etl_dags():
    weather_data_dict = extract()
    transform_res = transform(weather_data_dict)
    load(transform_res)

weather_etl_dags()