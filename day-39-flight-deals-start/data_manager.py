import os
from dotenv import load_dotenv
import requests
load_dotenv()


class DataManager:
    def __init__(self):
        self.sheet_data = {}
        self.url_sheety = os.environ.get("URL_SHEETY")
        self.sheety_key = os.environ.get("SHEETY_KEY")

    
    def get_sheet_data(self):
        
        response = requests.get(self.url_sheety, headers={"Authorization": f"Bearer {self.sheety_key}"})
        sheet_data = response.json()["prices"]
        return sheet_data
    
    def update_sheet_data(self, data):
        for line in data:
            update_url = f"{self.url_sheety}/{line['id']}"
            response = requests.put(update_url, json={"price": line}, headers={"Authorization": f"Bearer {self.sheety_key}"})
            
    
                #This class is responsible for talking to the Google Sheet.
    