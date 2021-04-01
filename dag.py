# Import libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Dict containing default args for the DAG
default_args = dict(...)

# Initialize DAG
dag = DAG(
    'tutorial',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1)
)

# Initialize bash operator tasks we want to perform
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag
)

# t2 depends on t1 running successfully to run
t1 >> t2
