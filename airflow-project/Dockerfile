FROM apache/airflow:3.0.0-python3.10

USER root
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
USER airflow
