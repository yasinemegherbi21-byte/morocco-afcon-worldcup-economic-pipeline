import pandas as pd
from pathlib import Path


def transform_host_cities():
    input_file = Path("data/raw/host_cities.csv")

    df = pd.read_csv(input_file)

    print("Original shape:", df.shape)
    print("Missing values:")
    print(df.isna().sum())

    df["population"] = pd.to_numeric(
        df["population"],
        errors="coerce"
    )

    df = df.sort_values(
        by="population",
        ascending=False
    )

    output_file = Path(
        "data/processed/host_cities_clean.csv"
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(output_file, index=False)

    print("Clean shape:", df.shape)
    print(
        f"Saved cleaned data to {output_file}"
    )

    return df


if __name__ == "__main__":
    transform_host_cities()