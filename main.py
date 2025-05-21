import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "habit0812"
pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "habit0812",
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# headers= {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()

user_input = input("How many kilometers did you run today? ")
pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers= {
    "X-USER-TOKEN": TOKEN
}
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": user_input,
}

response = requests.post(url=pixel_creation, json=post_params, headers=headers)

print(response.text)

# update_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
#
# data_change = {
#     "quantity": "7"
# }

# response = requests.put(url=update_delete_endpoint, json=data_change, headers=headers)
# print(response.text)

# response = requests.delete(url=update_delete_endpoint, headers=headers)
# print(response.text)