import smtplib
import os
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
    connection.sendmail(from_addr=EMAIL_ADDR,
                        to_addrs=EMAIL_RECV,
                        msg="Subject:Hello\n\nThis is the body of the email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

dob = dt.datetime(year=1991, month=7, day=17)
print(dob)
