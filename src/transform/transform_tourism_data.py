import pandas as pd
from pathlib import Path


def transform_tourism_data():
    input_file = Path("data/raw/worldbank_morocco_tourism.csv")

    df = pd.read_csv(input_file)

    print("Original shape:", df.shape)
    print("Missing values:")
    print(df.isna().sum())

    df["year"] = df["year"].astype(int)

    df = df.sort_values(
        by=["indicator_code", "year"],
        ascending=[True, True]
    )

    output_file = Path("data/processed/worldbank_morocco_tourism_clean.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)

    print("Clean shape:", df.shape)
    print(f"Saved cleaned data to {output_file}")

    return df


if __name__ == "__main__":
    transform_tourism_data()