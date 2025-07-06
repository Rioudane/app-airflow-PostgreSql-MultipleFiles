from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime
import pandas as pd
import subprocess
import os

# === CONFIG ===
DATA_DIR = "/opt/airflow/data"

CSV_FILE = next((os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith(".csv")), None)
if CSV_FILE is None:
    raise FileNotFoundError("No CSV file found in /opt/airflow/data.")

# Table name = file name without extension
TABLE_NAME = os.path.splitext(os.path.basename(CSV_FILE))[0]

# Path to store generated schema SQL
INIT_SQL_PATH = os.path.join(DATA_DIR, "init.sql")

MYSQL_CONN_ID = "mysql_default"


def generate_schema():
    cmd = f"csvsql --dialect mysql --tables {TABLE_NAME} {CSV_FILE} > {INIT_SQL_PATH}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"csvsql failed: {result.stderr}")
    print("Schema generated successfully.")


def create_table():
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    with open(INIT_SQL_PATH, "r") as f:
        sql = f.read()
    hook.run(sql)
    print(f"Table `{TABLE_NAME}` created successfully.")


def load_data():
    df = pd.read_csv(CSV_FILE)
    hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
    engine = hook.get_sqlalchemy_engine()
    df.to_sql(TABLE_NAME, con=engine, if_exists='append', index=False)
    print(f"Loaded {len(df)} rows into `{TABLE_NAME}`.")


# === DAG DEFINITION ===
with DAG(
        dag_id="csv_to_mysql_dag",
        start_date=datetime(2023, 1, 1),
        schedule_interval=None,
        catchup=False,
        tags=["csv", "mysql", "auto-schema"]
) as dag:

    task_generate_schema = PythonOperator(
        task_id="generate_schema",
        python_callable=generate_schema
    )

    task_create_table = PythonOperator(
        task_id="create_table",
        python_callable=create_table
    )

    task_load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    task_generate_schema >> task_create_table >> task_load_data
