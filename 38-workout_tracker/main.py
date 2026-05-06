from requests import *
import datetime
import os

URL_API = "https://app.100daysofpython.dev"


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
URL_SHEETY = os.environ.get("URL_SHEETY")
SHEETY_KEY = os.environ.get("SHEETY_KEY")



query_input = input("What exercise did you do? ")   



# os.environ["APP_ID"] = APP_ID
# print(os.environ["APP_ID"])
# os.environ["APP_KEY"] = APP_KEY
# os.environ["URL_SHEETY"] = URL_SHEETY
# os.environ["SHEETY_KEY"] = SHEETY_KEY

body = {
    "query": query_input,
    "weight_kg": 75,
    "height_cm": 176,                 
    "age": 41,
    "gender": "male"                 
}   

heders = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = post(f"{URL_API}/v1/nutrition/natural/exercise", json=body, headers=heders)
result = response.json()["exercises"][0]
# print(result)

sheety_header= {
    "Authorization": f"Bearer {SHEETY_KEY}"
}
sheety_body = {
    "workout": {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"]
    }
}

response = post(URL_SHEETY, headers=sheety_header, json=sheety_body)
print(response.text)
