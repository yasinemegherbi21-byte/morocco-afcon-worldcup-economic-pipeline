import pandas as pd
from pathlib import Path


def transform_infrastructure_data():
    input_file = Path("data/raw/infrastructure_projects.csv")

    df = pd.read_csv(input_file)

    print("Original shape:", df.shape)
    print("Missing values:")
    print(df.isna().sum())

    df["start_year"] = df["start_year"].astype(int)
    df["end_year"] = df["end_year"].astype(int)

    df = df.sort_values(
        by=["project_type", "city", "start_year"],
        ascending=[True, True, True]
    )

    output_file = Path("data/processed/infrastructure_projects_clean.csv")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False)

    print("Clean shape:", df.shape)
    print(f"Saved cleaned data to {output_file}")

    return df


if __name__ == "__main__":
    transform_infrastructure_data()