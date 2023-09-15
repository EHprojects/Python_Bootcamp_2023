import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv("../.idea/.env")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

rand_quote = random.choice(quotes)

now = dt.datetime.now()
current_dow = now.weekday()

if current_dow == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=EMAIL_RECV,
                            msg=f"Subject:Your Monday Motivational Quote\n\n{rand_quote}")

