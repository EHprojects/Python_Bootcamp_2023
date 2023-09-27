# from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests


# TWILIO_SID = YOUR TWILIO ACCOUNT SID
# TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
# TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
# TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER


load_dotenv("../.idea/.env")

# [Sheety]
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/users"

shty_head = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json",
}

class NotificationManager:

    def __init__(self):
        # self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        pass

    def send_sms(self, message):
        # message = self.client.messages.create(
        #     body=message,
        #     from_=TWILIO_VIRTUAL_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER,
        # )
        # # Prints if successfully sent.
        # print(message.sid)
        print("Simulated Message Sent")

    def send_email(self):
        pass
