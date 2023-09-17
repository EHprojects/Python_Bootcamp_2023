import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("../.idea/.env")

# API Info
OWM_API_KEY = os.getenv("OWM_API_KEY")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")

owm_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=owm_params)
response.raise_for_status()
weather_data = response.json()

hourly_dat = weather_data["hourly"]
twelve_hr_dat = hourly_dat[:12]

wx_codes = []
will_rain = False

for hour in twelve_hr_dat:
    wx_id = hour["weather"][0]["id"]
    wx_codes.append(wx_id)
    if wx_id < 700:
        will_rain = True

if will_rain:
    print("Bring your umbrella!")
