import requests
from datetime import datetime

MY_LAT = 38.945268884090176
MY_LONG = -77.09050927682685

params = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
