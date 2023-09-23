import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv("../.idea/.env")

# [NutritionixAPI]
NTX_APP_ID = os.getenv("NTX_APP_ID")
NTX_APP_KEY = os.getenv("NTX_APP_KEY")
NTX_GEND = os.getenv("NTX_GEND")
NTX_WGHT = os.getenv("NTX_WGHT")
NTX_HGHT = os.getenv("NTX_HGHT")
NTX_AGE = os.getenv("NTX_AGE")

# [Sheety]
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

exercises_completed = input("What exercises did you do today?: ")

ntx_head = {
    "x-app-id": NTX_APP_ID,
    "x-app-key": NTX_APP_KEY,
    "Content-Type": "application/json",
}

ntx_params = {
    "query": exercises_completed,
    "gender": NTX_GEND,
    "weight_kg": NTX_WGHT,
    "height_cm": NTX_HGHT,
    "age": NTX_AGE,
}

ntx_end = "https://trackapi.nutritionix.com/v2/natural/exercise"

ntx_resp = requests.post(url=ntx_end, headers=ntx_head, json=ntx_params)
# print(ntx_resp.json())

shty_end = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/workoutTracking/workouts"

# Date	        Time	    Exercise	Duration	Calories
# 21/07/2020	13:33:00	Running	    22	        130

now = datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M:%S")
exercises = ntx_resp.json()["exercises"]
# print(exercises)

for result in exercises:
    name = str(result["name"]).title()
    duration = result["duration_min"]
    calories = result["nf_calories"]
    # print(f"name: {name}, duration: {duration}, calories: {calories}")

    shty_head = {
        "Authorization": SHEETY_AUTH,
        "Content-Type": "application/json",

    }

    shty_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    shty_resp = requests.post(url=shty_end, headers=shty_head, json=shty_params)
    print(shty_resp.json())
