
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# Task function
def say_hello():
    print("Hello! My first Airflow DAG is running.")


# Create the DAG
with DAG(
    dag_id="hello_airflow_dag",
    start_date=datetime(2026, 1, 5),
    schedule="@daily",
    catchup=False,
) as dag:

    # Create a task
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=say_hello,
    )