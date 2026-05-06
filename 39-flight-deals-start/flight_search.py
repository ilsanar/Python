import json
import os, requests
from dotenv import load_dotenv

from datetime import datetime
from typing import Any

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.environ.get("SERPAPI_KEY")

    def check_flights(self, origin_city_code: str, destination_city_code: str, from_time: datetime, to_time: datetime) \
            -> dict[str, Any] | None:
        """Searches for flight options between two cities on specified departure dates
        using the SerpAPI.

        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date window start.
            to_time (datetime): The departure date window end. """

        # ddd = [str(from_time + timedelta(days=x)) for x in range((to_time - from_time).days + 1)]
        # departureDates = (", ".join(ddd))
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "EUR",
            "api_key": self._api_key
        }

        response = requests.get(SERPAPI_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://serpapi.com/google-flights-api")
            print("Response body:", response.text)
            return None
        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
    
    def save_flight_data(self, flight_data: dict[str, Any]) -> None:
        """Saves the flight data to a file for later use.

        Parameters:
            flight_data (dict): The flight data to be saved. """
        with open("flight_data.json", "a") as file:
            json.dump(flight_data, file, indent=4)