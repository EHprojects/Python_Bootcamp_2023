import requests
import os
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

# [Sheety]
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0a8227d1804e13b5bb2ff73b32ea070d/flightDeals/users"

shty_head = {
    "Authorization": SHEETY_AUTH,
    "Content-Type": "application/json",
}


class UserManager:

    def add_user(self, f_name, l_name, email):
        new_user = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email,
            }
        }

        response = requests.post(url=SHEETY_PRICES_ENDPOINT, headers=shty_head, json=new_user)
        print(response.json())
