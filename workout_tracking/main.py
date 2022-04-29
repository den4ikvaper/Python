import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
GENDER = "male"
AGE = 23
WEIGHT = 72.5
HEIGHT = 169
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/0d9244d7e0c9718a2981e99f34ff17a6/workoutTracking/workouts"

user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
}

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

sheety_headers = {
    "Authorization": os.environ['Bearer']
}

today_date = datetime.now().strftime("%Y/%m/%d")
today_time = datetime.now().strftime("%H:%M:%S")

for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
          'date': today_date,
          'time': today_time,
          'exercise': exercise['name'].title(),
          'duration': exercise['duration_min'],
          'calories': round(float(exercise['nf_calories'])),
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.text)