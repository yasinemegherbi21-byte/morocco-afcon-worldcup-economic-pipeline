# Morocco AFCON 2025 & FIFA World Cup 2030 Economic Impact Pipeline

## Project Overview

This project analyzes Morocco's economic growth, tourism development, infrastructure investments, and host-city preparations leading up to AFCON 2025 and the FIFA World Cup 2030.

The objective is to understand how Morocco is preparing for these major international sporting events through economic development, transportation improvements, stadium construction, airport expansion, and tourism growth.

The project combines Data Engineering, Data Analysis, and Machine Learning using a complete end-to-end pipeline.

---

## Project Objectives

* Analyze Morocco's economic indicators over time.
* Study tourism growth and tourism revenues.
* Explore infrastructure investments related to AFCON 2025 and the FIFA World Cup 2030.
* Analyze host cities selected for the events.
* Assess Morocco's event readiness using project timelines and infrastructure status.
* Demonstrate a complete Data Engineering workflow using ETL pipelines, PostgreSQL, Docker, Airflow, and Streamlit.

---

## Technologies Used

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Docker
* Apache Airflow
* Streamlit
* Plotly
* Scikit-Learn
* Git & GitHub

---

## Datasets

### Economic Indicators (World Bank API)

* GDP Growth (%)
* GDP Per Capita (Current US$)
* Inflation (%)
* Unemployment (%)
* Foreign Direct Investment (FDI)

### Tourism Indicators (World Bank API)

* International Tourism Arrivals
* International Tourism Receipts

### Infrastructure Projects

Infrastructure projects related to AFCON 2025 and FIFA World Cup 2030:

* Stadium Projects
* Airport Expansions
* Port Developments
* Railway Investments
* Urban Mobility Projects
* Road Infrastructure

### Host Cities

* Casablanca
* Rabat
* Tangier
* Marrakech
* Agadir
* Fes
* Benslimane

---

## ETL Pipeline

The project follows a traditional ETL process:

### Extract

Data is collected from World Bank APIs and curated infrastructure datasets.

### Transform

Data cleaning includes:

* Handling missing values
* Standardizing columns
* Formatting dates
* Preparing data for analysis

### Load

Cleaned data is loaded into PostgreSQL tables.

---

## PostgreSQL Database

Database:

morocco_events_db

Main Tables:

* economic_indicators
* tourism_data
* infrastructure_projects
* host_cities

---

## Airflow Workflow

Apache Airflow orchestrates the ETL pipeline.

Workflow:

Extract → Transform → Load

The DAG automates:

* Economic data processing
* Tourism data processing
* Infrastructure data processing
* Host city data processing

---

## Streamlit Dashboard

The Streamlit application provides:

* Economic indicators dashboard
* Tourism trends dashboard
* Infrastructure project analysis
* Host city analysis
* Event readiness monitoring
* Final project insights

---

## Key Findings

### Economy

* Morocco experienced long-term economic growth.
* GDP per capita increased significantly.
* Unemployment improved over time.
* Foreign direct investment increased despite yearly fluctuations.

### Tourism

* International tourism arrivals increased from approximately 2.7 million visitors to more than 13 million visitors.
* Tourism receipts increased from approximately $1.4 billion to nearly $10 billion.

### Infrastructure

* 19 major infrastructure projects were identified.
* Stadiums and airports represent the largest project categories.
* The Kenitra–Marrakech High Speed Rail project is the largest investment in the dataset.
* Nador West Med Port and Grand Stade Hassan II are major strategic investments.

### Event Readiness

* 9 projects are ongoing.
* 7 projects are planned.
* 3 projects are under construction.
* Project completion dates extend from 2025 to 2030, supporting Morocco's long-term preparation strategy.

---

## Machine Learning

### Machine Learning

A small Machine Learning component was included to explore the relationship between economic indicators and tourism performance.

Features used:

* GDP Growth
* GDP Per Capita
* Inflation
* Unemployment
* Foreign Direct Investment (FDI)

Target:

* International Tourism Arrivals

A Random Forest model was used as an exploratory approach and achieved an R² score of approximately 0.84.

It is important to note that the primary focus of this project is Data Engineering, data integration, and economic analysis rather than predictive modeling. The available dataset contains a limited number of yearly observations, making it unsuitable for building a robust production-grade forecasting model.

For this reason, Machine Learning was included as a supporting analytical component rather than the main objective of the project.


---

## Project Structure

```text
morocco-afcon-worldcup-economic-pipeline/

├── dags/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── extract/
│   ├── transform/
│   └── load/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Future Improvements


* Integrate live APIs.
* Deploy the Streamlit dashboard to the cloud.
* Expand infrastructure datasets.
* Build forecasting models using larger datasets.

---

## Conclusion

The project demonstrates how Data Engineering and Data Analytics can be used to study Morocco's preparation for AFCON 2025 and the FIFA World Cup 2030.

The results show strong tourism growth, continued economic development, significant infrastructure investments, and active preparation across multiple host cities. Together, these findings suggest that Morocco is making substantial investments to support both major sporting events and long-term national development.
