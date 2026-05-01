from datetime import *
import requests
import smtplib

MY_LAT = 51.593151
MY_LNG = 4.522886


def iss_above():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])

    # print(longitude, MY_LNG + 5, MY_LNG - 5)
    # print(latitude, MY_LAT + 5, MY_LAT - 5)
    if MY_LAT + 5 > latitude > MY_LAT - 5 and MY_LNG + 5 > longitude > MY_LNG - 5:
        return( True)
    else:
        return( False )


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": "Europe/Amsterdam"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour

    # print(sunset, current_hour, sunrise)
   
    if  current_hour > sunset or current_hour < sunrise: 
    
        return( True)
    else:
        return( False)


def send_email():
    my_email = "p.palat@samsung.com"
    password = "Trouble01!"
    msg = f"Subject: Look Up!\n\nIf there is a good weather you can see ISS in the sky"
    with  smtplib.SMTP("smtp.w1.samsung.net", 25) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs= my_email,
                            msg=msg)

if iss_above() and is_night():
    send_email()