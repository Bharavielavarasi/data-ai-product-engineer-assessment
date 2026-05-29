# Task 2 — Weather Data Pipeline

## Objective

Build a simple data pipeline that fetches weather data from a public API, transforms it, and stores it in BigQuery.

## Data Source

Open-Meteo API

Location:
- Chennai, India
- Latitude: 13.0827
- Longitude: 80.2707

## Pipeline Steps

1. Fetch weather data from Open-Meteo API
2. Parse JSON response
3. Convert data into tabular format
4. Create derived field: temperature_category
5. Store data in BigQuery
6. Query data using SQL

## Schema

| Field | Type |
|---------|---------|
| date | DATE |
| max_temperature | FLOAT |
| min_temperature | FLOAT |
| temperature_category | STRING |

## Transformation Logic

- Hot → temperature > 35°C
- Warm → temperature between 25°C and 35°C
- Cold → temperature < 25°C

## Future Improvements

- Automated scheduling using Airflow
- Monitoring and alerting
- Data quality checks
- Incremental loading
- CI/CD deployment
