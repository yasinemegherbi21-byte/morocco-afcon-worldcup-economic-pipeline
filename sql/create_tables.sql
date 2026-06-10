CREATE TABLE IF NOT EXISTS economic_indicators (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    indicator_code VARCHAR(50),
    indicator_name VARCHAR(255),
    year INTEGER,
    value NUMERIC,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS tourism_data (
    id SERIAL PRIMARY KEY,
    year INTEGER,
    tourist_arrivals NUMERIC,
    tourism_receipts NUMERIC,
    hotel_capacity NUMERIC,
    occupancy_rate NUMERIC,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS infrastructure_projects (
    id SERIAL PRIMARY KEY,
    project_name VARCHAR(255),
    city VARCHAR(100),
    project_type VARCHAR(100),
    investment_amount NUMERIC,
    status VARCHAR(50),
    start_year INTEGER,
    end_year INTEGER,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stadium_projects (
    id SERIAL PRIMARY KEY,
    stadium_name VARCHAR(255),
    city VARCHAR(100),
    capacity INTEGER,
    status VARCHAR(50),
    budget NUMERIC,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS host_cities (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    event_name VARCHAR(100),
    region VARCHAR(100),
    population NUMERIC,
    source VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
