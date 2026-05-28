import requests
import pandas as pd
import logging

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

    print(df)

except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")
