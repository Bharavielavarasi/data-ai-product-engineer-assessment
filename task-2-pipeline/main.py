import requests
import pandas as pd
import logging
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)

API_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}

try:
    logging.info("Fetching weather data...")

    response = requests.get(API_URL, params=params)

    response.raise_for_status()

    data = response.json()

    daily_data = data["daily"]

    df = pd.DataFrame({
        "date": daily_data["time"],
        "max_temperature": daily_data["temperature_2m_max"],
        "min_temperature": daily_data["temperature_2m_min"]
    })

    df["temperature_category"] = df["max_temperature"].apply(
        lambda x: "Hot" if x > 35 else "Warm" if x > 25 else "Cold"
    )

    print(df)
    client = bigquery.Client.from_service_account_json(
    "weather-data-497718-9f961d3fb8d2.json"
    )

    table_id = "weather-data-497718.weather_dataset.weather_data"

    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print("Data loaded successfully into BigQuery!")

except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")
