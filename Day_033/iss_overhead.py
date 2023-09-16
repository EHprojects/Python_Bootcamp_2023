import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv("../.idea/.env")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")

MY_LAT = 38.945268884090176
MY_LONG = -77.09050927682685


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_dark():
    params = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False


def send_mail_notif():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=EMAIL_RECV,  # change to "email"
                            msg=f"Look Up!\n\nThe ISS is overhead!")


def check_iss():
    if iss_overhead() and is_dark():
        send_mail_notif()


while True:
    check_iss()
    time.sleep(60)
