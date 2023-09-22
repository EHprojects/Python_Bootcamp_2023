import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("../.idea/.env")

# Pixela API Info
PIX_API_TOKEN = os.getenv("PIX_API_TOKEN")
PIX_USER_NAME = os.getenv("PIX_USER_NAME")
GRAPH_ID = "graph1"

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

yesterday = datetime(year=2023, month=9, day=20)
yesterday = yesterday.strftime("%Y%m%d")

pixel_post_params = {
    "date": yesterday,
    "quantity": "20"
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(response.text)

pixel_update_params = {
    "quantity": "24"
}

pixel_update_end = f"{pixela_endpoint}/{PIX_USER_NAME}/graphs/{GRAPH_ID}/{yesterday}"

# Update
# response = requests.put(url=pixel_update_end, json=pixel_update_params, headers=headers)
# print(response.text)

# Delete
response = requests.delete(url=pixel_update_end, headers=headers)
print(response.text)
