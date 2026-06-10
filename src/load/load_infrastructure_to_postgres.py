import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


def load_infrastructure_data():
    df = pd.read_csv(
        "data/processed/infrastructure_projects_clean.csv"
    )

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    with engine.begin() as conn:
        conn.execute(
            text("TRUNCATE TABLE infrastructure_projects RESTART IDENTITY")
        )

    df.to_sql(
        "infrastructure_projects",
        engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(df)} rows into infrastructure_projects"
    )


if __name__ == "__main__":
    load_infrastructure_data()