from __future__ import annotations
from airflow.decorators import task
import logging

@task()
def load(transform_res: list):
    logging.info(transform_res)
