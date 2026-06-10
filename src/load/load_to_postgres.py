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


def load_data_to_postgres():
    df = pd.read_csv(
        "data/processed/worldbank_morocco_indicators_clean.csv"
    )

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    with engine.begin() as conn:
        conn.execute(
            text("TRUNCATE TABLE economic_indicators RESTART IDENTITY")
        )

    df.to_sql(
        "economic_indicators",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows into economic_indicators")


if __name__ == "__main__":
    load_data_to_postgres()