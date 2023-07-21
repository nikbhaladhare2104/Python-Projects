import requests
from datetime import datetime


END_USER = "https://pixe.la/v1/users"
TOKEN = "YOUR_TOKEN"
USERNAME = "YOUR_USERNAME"
GRAPH_ID = "GRAPH_ID"

END_GRAPH = f"{END_USER}/{USERNAME}/graphs"

para = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=END, json=para)
# print(response.text)

para_graph = {
    "id": GRAPH_ID,
    "name": "running graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=END_GRAPH, json=para_graph, headers=headers)
# print(response.text)
# l = 5
# for i in range(10):
# today = datetime(year=2023, month=6, day=5+i)
# print(today.strftime("%Y%m%d"))
# l+=1
today = datetime.now()
PIXEL_END = F"{END_GRAPH}/{GRAPH_ID}"

para_pixel = {
    "name": GRAPH_ID,
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today? ")
}

response = requests.post(url=PIXEL_END, json=para_pixel, headers=headers)
# response = requests.put(url=PIXEL_END, json=para_pixel, headers=headers)
print(response.text)

