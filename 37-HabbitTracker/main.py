import requests
import datetime as dt
import os

TOKEN = os.environ["PIXELA_TOKEN"]
USER = os.environ["PIXELA_USER"]
GRAPH_ID = os.environ["PIXELA_GRAPH_ID"]

TODAY = dt.date.today().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
"username":USER,	
"agreeTermsOfService":"yes",	
"notMinor":"yes",   
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name":"My excersizes",
    "unit":"minute",
    "type":"int",
    "color":"sora",
    "timezone":"Europe/Amsterdam",
    "startOnMonday":True
}

headers = {
    
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config={
    "date":TODAY,
    "quantity":"45"   
}
# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)


specific_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{TODAY}"
new_pixel_config={
    
    "quantity":"120"   
}

# response = requests.put(url=specific_pixel_endpoint,json=new_pixel_config,headers=headers)
# print(response.text)


response = requests.delete(url=specific_pixel_endpoint,headers=headers)
print(response.text)