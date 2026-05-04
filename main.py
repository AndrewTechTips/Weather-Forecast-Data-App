import streamlit as st
import plotly.express as px
from streamlit import context

from backend import get_data

st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

# Add title, text input, slider, selectbox, and subheader
st.title("⛅ Weather Forecast")

place = st.text_input("Place: ")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days",
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.divider()

# Get the temperature/sky data
if place:
    st.subheader(f"{option} for the next {days} days in {place.title()}")
    filtered_data = get_data(place, days)

    if not filtered_data:
        st.error("That place does not exist or there was an API error.")

    else:
        if option == "Temperature":
            temperatures = [entry["main"]["temp"] for entry in filtered_data]
            dates = [entry["dt_txt"][:16] for entry in filtered_data]

            # Create a temperature plot
            figure = px.line(
                x=dates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (C)"},
                line_shape="spline",
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
            image_paths = [
                images.get(condition, "assets/cloud.png")
                for condition in sky_conditions
            ]
            dates = [
                entry["dt_txt"][:16].replace(" ", " | ") for entry in filtered_data
            ]

            st.markdown(
                """
                            <style>
                            div[data-testid="stImage"] {
                                display: flex;
                                justify-content: center;
                                flex-wrap: wrap;
                            }
                            </style>
                        """,
                unsafe_allow_html=True,
            )

            st.image(image_paths, width=115, caption=dates)
else:
    st.info("👆 Please enter a city name above to see the forecast.")
