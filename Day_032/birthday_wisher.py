import smtplib
import os
import pandas
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv("../.idea/.env")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")

now = dt.datetime.now()
this_month = now.month
today = now.day

letters = []

for file_name in os.listdir("./letter_templates"):
    with open(f"./letter_templates/{file_name}", "r") as file:
        letter = file.read()
        letters.append(letter)

birthday_dat = pandas.read_csv("birthdays.csv")
# birthday_dat = birthday_dat.to_dict(orient="records")
for idx, row in birthday_dat.iterrows():
    if row.month == this_month and row.day == today:
        name = row["name"]
        email = row["email"]
        rand_letter = random.choice(letters)
        rand_letter = rand_letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
            connection.sendmail(from_addr=EMAIL_ADDR,
                                to_addrs=EMAIL_RECV,  # change to "email"
                                msg=f"Subject:Happy Birthday!\n\n{rand_letter}")
