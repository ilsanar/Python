import requests
import os
from twilio.rest import Client




API_KEY_OPENWEATHERMAP=os.environ["API_KEY_OPENWEATHERMAP"]
MY_LNG = 4.522886
MY_LAT = 51.593633

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY_OPENWEATHERMAP,
    "units":"metric",
    "cnt":4}

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
data.raise_for_status()
will_rain = False
for item in data.json()["list"]:
    condition_code = int(item["weather"][0]["id"])
    if condition_code <700:
        will_rain = True

if will_rain == True:
   client = Client(account_sid, auth_token)
   message = client.messages.create(
    body="It's going to rain. Take umbrella ela ela ela...",
    from_="whatsapp:+14155238886",
    to="whatsapp:+31653131416",
)

print(message.status)
            