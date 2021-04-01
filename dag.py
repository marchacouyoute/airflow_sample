# Import libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = dict(...)
