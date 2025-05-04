from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaConsumer
import json

def consume_kafka():
    consumer = KafkaConsumer(
        'mock_photovoltaic',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='airflow-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        print("Received:", message.value)
        break  # Pour éviter une boucle infinie

with DAG(
    dag_id='kafka_consumer_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@once',
    catchup=False,
    tags=['kafka'],
) as dag:
    consume_task = PythonOperator(
        task_id='consume_kafka',
        python_callable=consume_kafka
    )
