import requests
import streamlit as st

API_KEY = st.secrets["API_KEY"]


def get_data(place: str, forecast_days: int = 1) -> list:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        return []

    filtered_data = data["list"]
    nr_values = 8 * forecast_days

    return filtered_data[:nr_values]


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
