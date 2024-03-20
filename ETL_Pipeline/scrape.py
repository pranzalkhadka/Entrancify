from airflow.decorators import dag
from airflow.operators.python import PythonOperator
import pendulum
import json
from extract import Extract
from transform import Transform
from load import Load

def create_extract_transform_load_tasks(college_info):
    extract_task = PythonOperator(
        task_id=f'Extract_data_{college_info["name"]}',
        python_callable=Extract().extract,
        op_args=[college_info["url"], college_info["html_file_path"]]
    )

    transform_task = PythonOperator(
        task_id=f'Transform_data_{college_info["name"]}',
        python_callable=Transform().transform,
        op_args=[college_info["html_file_path"], college_info["csv_file_path"]]
    )

    load_task = PythonOperator(
        task_id=f'Load_warehouse_table_{college_info["name"]}',
        python_callable=Load().load,
        op_args=[college_info["csv_file_path"], college_info["schema"], college_info["table"]]
    )

    return extract_task, transform_task, load_task

@dag(
    dag_id='scrape',
    schedule_interval='@daily',
    start_date=pendulum.datetime(2024, 3, 5),
    catchup=False
)
def scrape():
    with open('/home/pranjal/airflow/dags/config.json') as f:
        config = json.load(f)

    for college_info in config["colleges"]:
        extract_task, transform_task, load_task = create_extract_transform_load_tasks(college_info)
        extract_task >> transform_task >> load_task

webscrape = scrape()
