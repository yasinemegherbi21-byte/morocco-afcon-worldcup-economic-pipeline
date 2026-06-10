import requests
import pandas as pd
from pathlib import Path


COUNTRY_CODE = "MAR"

INDICATORS = {
    "NY.GDP.MKTP.KD.ZG": "GDP growth annual %",
    "NY.GDP.PCAP.CD": "GDP per capita current US$",
    "FP.CPI.TOTL.ZG": "Inflation consumer prices annual %",
    "SL.UEM.TOTL.ZS": "Unemployment total %",
    "BX.KLT.DINV.CD.WD": "Foreign direct investment net inflows",
}


def fetch_worldbank_indicator(indicator_code, indicator_name):
    url = (
        f"https://api.worldbank.org/v2/country/{COUNTRY_CODE}/indicator/"
        f"{indicator_code}?format=json&per_page=100"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()[1]

    rows = []

    for item in data:
        rows.append(
            {
                "country": item["country"]["value"],
                "indicator_code": indicator_code,
                "indicator_name": indicator_name,
                "year": int(item["date"]),
                "value": item["value"],
                "source": "World Bank API",
            }
        )

    return pd.DataFrame(rows)


def extract_all_indicators():
    all_data = []

    for code, name in INDICATORS.items():
        print(f"Extracting {name}...")
        df = fetch_worldbank_indicator(code, name)
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    output_path = Path("data/raw/worldbank_morocco_indicators.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    final_df.to_csv(output_path, index=False)

    print(f"Saved data to {output_path}")
    print(final_df.head())


if __name__ == "__main__":
    extract_all_indicators()