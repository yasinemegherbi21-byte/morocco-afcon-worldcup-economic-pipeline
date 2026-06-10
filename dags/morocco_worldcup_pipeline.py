from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_PATH = "/opt/airflow"

with DAG(
    dag_id="morocco_worldcup_economic_pipeline",
    description="Morocco AFCON 2025 & World Cup 2030 Economic Pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["morocco", "worldcup", "etl"],
) as dag:

    # Economic Indicators
    extract_economic_data = BashOperator(
        task_id="extract_economic_data",
        bash_command=f"cd {PROJECT_PATH} && python src/extract/extract_worldbank.py",
    )

    transform_economic_data = BashOperator(
        task_id="transform_economic_data",
        bash_command=f"cd {PROJECT_PATH} && python src/transform/transform_economic_data.py",
    )

    load_economic_data = BashOperator(
        task_id="load_economic_data",
        bash_command=f"cd {PROJECT_PATH} && python src/load/load_to_postgres.py",
    )

    # Tourism
    extract_tourism_data = BashOperator(
        task_id="extract_tourism_data",
        bash_command=f"cd {PROJECT_PATH} && python src/extract/extract_tourism_data.py",
    )

    transform_tourism_data = BashOperator(
        task_id="transform_tourism_data",
        bash_command=f"cd {PROJECT_PATH} && python src/transform/transform_tourism_data.py",
    )

    load_tourism_data = BashOperator(
        task_id="load_tourism_data",
        bash_command=f"cd {PROJECT_PATH} && python src/load/load_tourism_to_postgres.py",
    )

    # Infrastructure
    transform_infrastructure_data = BashOperator(
        task_id="transform_infrastructure_data",
        bash_command=f"cd {PROJECT_PATH} && python src/transform/transform_infrastructure_data.py",
    )

    load_infrastructure_data = BashOperator(
        task_id="load_infrastructure_data",
        bash_command=f"cd {PROJECT_PATH} && python src/load/load_infrastructure_to_postgres.py",
    )

    # Host Cities
    transform_host_cities = BashOperator(
        task_id="transform_host_cities",
        bash_command=f"cd {PROJECT_PATH} && python src/transform/transform_host_cities.py",
    )

    load_host_cities = BashOperator(
        task_id="load_host_cities",
        bash_command=f"cd {PROJECT_PATH} && python src/load/load_host_cities_to_postgres.py",
    )

    (
        extract_economic_data
        >> transform_economic_data
        >> load_economic_data
        >> extract_tourism_data
        >> transform_tourism_data
        >> load_tourism_data
        >> transform_infrastructure_data
        >> load_infrastructure_data
        >> transform_host_cities
        >> load_host_cities
    )