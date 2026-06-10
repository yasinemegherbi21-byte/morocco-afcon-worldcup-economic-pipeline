-- Total number of records
SELECT COUNT(*) AS total_records
FROM economic_indicators;


-- Distinct indicators
SELECT DISTINCT indicator_name
FROM economic_indicators;


-- Number of records per indicator
SELECT
    indicator_name,
    COUNT(*) AS record_count
FROM economic_indicators
GROUP BY indicator_name
ORDER BY record_count DESC;


-- Most recent data available
SELECT *
FROM economic_indicators
ORDER BY year DESC
LIMIT 10;


-- GDP Growth only
SELECT
    year,
    value
FROM economic_indicators
WHERE indicator_name = 'GDP growth annual %'
ORDER BY year DESC; 

-- Total infrastructure investment by city
SELECT
    city,
    SUM(investment_amount) AS total_investment
FROM infrastructure_projects
WHERE investment_amount IS NOT NULL
GROUP BY city
ORDER BY total_investment DESC;