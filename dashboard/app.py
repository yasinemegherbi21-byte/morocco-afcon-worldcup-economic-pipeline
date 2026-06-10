import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine


# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Morocco AFCON 2025 & World Cup 2030 Dashboard",
    layout="wide"
)

st.title("🇲🇦 Morocco AFCON 2025 & FIFA World Cup 2030 Economic Dashboard")

st.markdown(
    """
    This dashboard analyzes Morocco's economic, tourism, infrastructure,
    and host-city preparation for AFCON 2025 and the FIFA World Cup 2030.
    """
)


# =========================
# Database Connection
# =========================
DB_USER = "yassine"
DB_PASSWORD = "morocco2030"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "morocco_events_db"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


@st.cache_data
def load_data():
    economic_df = pd.read_sql("SELECT * FROM economic_indicators", engine)
    tourism_df = pd.read_sql("SELECT * FROM tourism_data", engine)
    infrastructure_df = pd.read_sql("SELECT * FROM infrastructure_projects", engine)
    host_cities_df = pd.read_sql("SELECT * FROM host_cities", engine)

    return economic_df, tourism_df, infrastructure_df, host_cities_df


economic_df, tourism_df, infrastructure_df, host_cities_df = load_data()


# =========================
# Sidebar
# =========================
st.sidebar.title("Dashboard Sections")

section = st.sidebar.radio(
    "Choose a section",
    [
        "Overview",
        "Economic Indicators",
        "Tourism",
        "Infrastructure",
        "Host Cities",
        "Event Readiness",
        "Final Insights"
    ]
)


# =========================
# Overview
# =========================
if section == "Overview":
    st.header("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Economic Records", len(economic_df))
    col2.metric("Tourism Records", len(tourism_df))
    col3.metric("Infrastructure Projects", len(infrastructure_df))
    col4.metric("Host Cities", len(host_cities_df))

    st.subheader("Project Purpose")

    st.write(
        """
        This project studies Morocco's preparation for AFCON 2025 and the FIFA World Cup 2030
        through economic indicators, tourism performance, infrastructure investments,
        and host-city readiness.
        """
    )

    st.subheader("Main Data Engineering Stack")

    st.write(
        """
        Python, PostgreSQL, Docker, ETL pipelines, SQL, Apache Airflow, Streamlit, and Machine Learning.
        """
    )


# =========================
# Economic Indicators
# =========================
elif section == "Economic Indicators":
    st.header("Economic Indicators Analysis")

    indicators = economic_df["indicator_name"].unique()

    selected_indicator = st.selectbox(
        "Select an economic indicator",
        indicators
    )

    filtered_df = economic_df[
        economic_df["indicator_name"] == selected_indicator
    ].dropna(subset=["value"])

    fig = px.line(
        filtered_df,
        x="year",
        y="value",
        title=f"{selected_indicator} Over Time",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Summary Statistics")
    st.dataframe(filtered_df[["year", "value"]].describe())

    st.info(
        """
        Economic indicators help understand Morocco's long-term economic context
        before AFCON 2025 and the FIFA World Cup 2030.
        """
    )


# =========================
# Tourism
# =========================
elif section == "Tourism":
    st.header("Tourism Analysis")

    tourism_indicators = tourism_df["indicator_name"].unique()

    selected_tourism = st.selectbox(
        "Select a tourism indicator",
        tourism_indicators
    )

    tourism_filtered = tourism_df[
        tourism_df["indicator_name"] == selected_tourism
    ].dropna(subset=["value"])

    display_df = tourism_filtered.copy()

    if "receipts" in selected_tourism.lower():
        display_df["display_value"] = display_df["value"] / 1_000_000_000
        y_label = "Billion US$"
    else:
        display_df["display_value"] = display_df["value"] / 1_000_000
        y_label = "Million Visitors"

    fig = px.line(
        display_df,
        x="year",
        y="display_value",
        title=f"{selected_tourism} Over Time",
        markers=True,
        labels={"display_value": y_label}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        Tourism arrivals and receipts show Morocco's growing international attractiveness
        before the upcoming major sporting events.
        """
    )


# =========================
# Infrastructure
# =========================
elif section == "Infrastructure":
    st.header("Infrastructure Projects")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Projects", len(infrastructure_df))
    col2.metric(
        "Verified Investment",
        f"{infrastructure_df['investment_amount'].sum() / 1_000_000_000:.1f}B MAD"
    )
    col3.metric(
        "Project Types",
        infrastructure_df["project_type"].nunique()
    )

    st.subheader("Projects by Type")

    project_type_counts = (
        infrastructure_df["project_type"]
        .value_counts()
        .reset_index()
    )

    project_type_counts.columns = ["project_type", "count"]

    fig = px.bar(
        project_type_counts,
        x="project_type",
        y="count",
        title="Infrastructure Projects by Type"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Largest Verified Investments")

    investment_df = infrastructure_df[
        infrastructure_df["investment_amount"].notna()
    ].sort_values(
        by="investment_amount",
        ascending=False
    )

    investment_display = investment_df[
        ["project_name", "city", "project_type", "investment_amount"]
    ].copy()

    investment_display["investment_billion_mad"] = (
        investment_display["investment_amount"] / 1_000_000_000
    )

    st.dataframe(
        investment_display[
            ["project_name", "city", "project_type", "investment_billion_mad"]
        ]
    )

    fig = px.bar(
        investment_display,
        x="project_name",
        y="investment_billion_mad",
        title="Largest Infrastructure Investments",
        labels={"investment_billion_mad": "Investment (Billion MAD)"}
    )

    st.plotly_chart(fig, use_container_width=True)


# =========================
# Host Cities
# =========================
elif section == "Host Cities":
    st.header("Host Cities")

    st.dataframe(host_cities_df[["city", "region", "population", "event_name"]])

    fig = px.bar(
        host_cities_df.sort_values("population", ascending=False),
        x="city",
        y="population",
        title="Host City Population"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        """
        The host cities include major urban centers across Morocco,
        supporting the national scale of AFCON 2025 and World Cup 2030 preparation.
        """
    )


# =========================
# Event Readiness
# =========================
elif section == "Event Readiness":
    st.header("Event Infrastructure Readiness")

    st.subheader("Project Status")

    status_counts = (
        infrastructure_df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ["status", "count"]

    fig = px.pie(
        status_counts,
        names="status",
        values="count",
        title="Infrastructure Project Status"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Project Completion Timeline")

    timeline_counts = (
        infrastructure_df["end_year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    timeline_counts.columns = ["end_year", "count"]

    fig = px.bar(
        timeline_counts,
        x="end_year",
        y="count",
        title="Expected Project Completion by Year"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Projects Timeline Table")

    st.dataframe(
        infrastructure_df[
            ["project_name", "city", "project_type", "status", "start_year", "end_year"]
        ].sort_values("end_year")
    )


# =========================
# Final Insights
# =========================
elif section == "Final Insights":
    st.header("Final Insights")

    st.markdown(
        """
        ### Key Findings

        - Morocco shows long-term economic development through GDP per capita growth.
        - Tourism arrivals and receipts increased strongly before the COVID-19 shock.
        - Infrastructure preparation includes stadiums, airports, ports, railways, roads, and urban mobility.
        - The largest verified investment is the Kenitra–Marrakech High Speed Rail project.
        - Stadiums and airports are the most common infrastructure project categories.
        - Project completion dates extend from 2025 to 2030, showing a phased preparation strategy.
        - The preparation is not only for sporting events, but also supports long-term economic development.
        """
    )
