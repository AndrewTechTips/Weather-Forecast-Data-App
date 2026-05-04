<div align="center">

  <h1>⛅ Weather Forecast</h1>

  <p>
    A <strong>multi-day weather forecast app</strong> built with Python and Streamlit.<br />
    Search any city, pick a forecast range, and view either a <strong>temperature chart</strong> or <strong>sky condition icons</strong> — powered by the OpenWeatherMap API.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
    <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
    <img src="https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge" alt="OpenWeatherMap" />
  </p>

  <h3>
    <a href="#">🌤️ OPEN APP</a>
  </h3>

</div>

<br />

---

## ✨ Features

* **🔍 City Search:** Enter any city name to fetch its forecast data instantly.
* **📅 1–5 Day Forecast:** A slider controls how many days ahead to display — data is fetched in 3-hour intervals.
* **📈 Temperature Chart:** An interactive Plotly spline chart shows temperature over time.
* **🌥️ Sky View:** Switches to a grid of weather icons (Clear, Clouds, Rain, Snow) with timestamps as captions.
* **⚠️ Error Handling:** Invalid or unknown cities show a clean error message instead of crashing.

---

## 🧠 Under the Hood

### Backend (`backend.py`)
The OpenWeatherMap `/forecast` endpoint returns data in 3-hour slots — 8 per day. The function slices the list based on the number of requested days:

```python
def get_data(place: str, forecast_days: int = 1) -> list:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    filtered_data = data["list"]
    nr_values = 8 * forecast_days   # 8 slots × n days
    return filtered_data[:nr_values]
```

### Temperature View
Temperatures and timestamps are extracted from the response and plotted with a smooth Plotly spline line:

```python
temperatures = [entry["main"]["temp"] for entry in filtered_data]
dates = [entry["dt_txt"][:16] for entry in filtered_data]
figure = px.line(x=dates, y=temperatures, line_shape="spline")
```

### Sky View
Weather condition strings are mapped to local icon files in `assets/` — unknown conditions fall back to the cloud icon:

```python
images = {"Clear": "assets/clear.png", "Clouds": "assets/cloud.png",
          "Rain": "assets/rain.png",   "Snow": "assets/snow.png"}

image_paths = [images.get(condition, "assets/cloud.png") for condition in sky_conditions]
```

---

## 📁 Project Structure

```
Weather-Forecast/
├── assets/
│   ├── clear.png
│   ├── cloud.png
│   ├── rain.png
│   └── snow.png
├── backend.py    # OpenWeatherMap API call & data slicing
├── main.py       # Streamlit UI — chart & sky views
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndrewTechTips/Weather-Forecast.git
    cd Weather-Forecast
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your API key** in `backend.py`:
    ```python
    API_KEY = "your_openweathermap_api_key"
    ```
    > ⚠️ Get a free key at [openweathermap.org](https://openweathermap.org/api). Store it as an environment variable in production — never commit it to GitHub.

4. **Run the app:**
    ```bash
    streamlit run main.py
    ```

---

## 📬 Contact

* **LinkedIn:** [Andrei Condrea](https://www.linkedin.com/in/andrei-condrea-b32148346)
* **Email:** condrea.andrey777@gmail.com

<p align="center">
  <i>"Always check the forecast before you ship." ⛅</i>
</p>