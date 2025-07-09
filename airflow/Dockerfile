FROM apache/airflow:2.7.1

COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

USER root
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir psycopg2-binary requests csvkit
