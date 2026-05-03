import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days",
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Get the temperature/sky data
if place:
    filtered_data = get_data(place, days)

    if not filtered_data:
        st.error("That place does not exist or there was an API error.")

    else:
        if option == "Temperature":
            temperatures = [entry["main"]["temp"] for entry in filtered_data]
            dates = [entry["dt_txt"] for entry in filtered_data]

            # Create a temperature plot
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"}
            )
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "assets/clear.png",
                "Clouds": "assets/cloud.png",
                "Rain": "assets/rain.png",
                "Snow": "assets/snow.png",
            }

            sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            dates = [entry["dt_txt"] for entry in filtered_data]

            st.image(image_paths, width=115, caption=dates)
