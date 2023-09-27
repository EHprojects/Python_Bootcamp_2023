import requests
import os
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

# [Sheety]
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/prices"

shty_head = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=shty_head)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=shty_head,
                json=new_data,
            )
            print(response.text)
