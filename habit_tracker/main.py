import requests
from datetime import datetime, timedelta
from random import randint

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "den4ikvaper"
TOKEN = "hgfytrhg"
GRAPH_ID = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN,
}

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
#

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today_date = datetime.now()
i = 0

for _ in range(400):
    today_date = datetime.now() - timedelta(days=i)
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    pixel_data = {
        "date": today_date.strftime("%Y%m%d"),
        "quantity": f"{randint(1,10)}.{randint(1,99)}",
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)
    i += 1

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "4.5",
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)



