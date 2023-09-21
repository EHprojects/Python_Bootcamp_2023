import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("../.idea/.env")

# Pixela API Info
PIX_API_TOKEN = os.getenv("PIX_API_TOKEN")
PIX_USER_NAME = os.getenv("PIX_USER_NAME")

pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{PIX_USER_NAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Japanese Studying",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji"
# }

headers = {
    "X-USER-TOKEN": PIX_API_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/graph1"

pixel_post_params = {
    "date": "20230920",
    "quantity": "22"
}

