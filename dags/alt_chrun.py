# скопируйте код ниже #
# dags/alt_churn.py
from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from steps.churn import extract, transform, load, create_table # импортируем фукнции с логикой шагов
from steps.messages import send_telegram_failure_message,send_telegram_success_message
# продолжите код и запустите его в виртуальной машине #
# после отработки кода нажмите кнопку Проверить, добавлять свое решение необязательно #

with DAG(
    dag_id='alt_churn',
    schedule='@once',
    tags=['ETL_ALT'],
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    on_success_callback=send_telegram_success_message,
    on_failure_callback=send_telegram_failure_message
) as dag:
    create_table_step = PythonOperator(task_id='create_table', python_callable=create_table)
    extract_step = PythonOperator(task_id='extract', python_callable=extract)
    transform_step = PythonOperator(task_id='transform', python_callable=transform)
    load_step = PythonOperator(task_id='load', python_callable=load)
    
    create_table_step >> extract_step >> transform_step >> load_step