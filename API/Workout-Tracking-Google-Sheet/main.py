import requests
from datetime import datetime

API_ID = "YOUR_API_ID"
API_KEY = "YOUR_API_KEY"


END = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END = "https://api.sheety.co/a17baf3d16768d0d4b540037916dea24/myWorkouts/workouts"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
QUERY = input("How much did you ran today: ")
para = {
     "query": QUERY,
     "gender": "YOUR_GENDER",
     "weight_kg": YOUR_WEIGHT, # should be int
     "height_cm": YOUR_HEIGHT, # SHOULD BE INT
     "age": YOUR_AGE  # SHOULD BE INT 
}
response = requests.post(END, json=para, headers=headers)
data = response.json()
# print(data)

""""----------------------------"""

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_END, json=sheet_inputs)



