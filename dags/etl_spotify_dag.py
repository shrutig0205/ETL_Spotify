from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add the path of the tasks folder to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tasks')))

# Import task functions
from extract_spotify_data import get_token, search_indian_indie_songs
from transform_spotify_data import process_spotify_response
from load_spotify_data import upload_to_s3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spotify_etl_dag',
    default_args=default_args,
    description='Spotify ETL DAG',
    schedule_interval=timedelta(days=1),
)

def extract_task():
    token = get_token()
    return search_indian_indie_songs(token)

def transform_task(ti):
    tracks = ti.xcom_pull(task_ids='extract_task')
    return process_spotify_response(tracks)

def load_task(ti):
    df = ti.xcom_pull(task_ids='transform_task')
    upload_to_s3(df)

extract = PythonOperator(
    task_id='extract_task',
    python_callable=extract_task,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform_task',
    python_callable=transform_task,
    dag=dag,
)

load = PythonOperator(
    task_id='load_task',
    python_callable=load_task,
    dag=dag,
)

extract >> transform >> load
