
import os, requests

from dotenv import load_dotenv


load_dotenv()
URL_TOKEN = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
CITY_CODE_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    
class FlightSearch:
    
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_KEY")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        self._token = self._get_new_token()
    
    def _get_new_token(self):
       
        self.headers_token = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.body_token = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(URL_TOKEN, headers=self.headers_token, data=self.body_token)
        self._token = response.json()["access_token"]
        return self._token
        
    def get_destination_code(self, city):
       
        headers_city_code = {
            "Authorization": f"Bearer {self._get_new_token()}"
        }
        params_city_code = {
            "keyword": city,
            "max": 1
        }
        response = requests.get(CITY_CODE_ENDPOINT, headers=headers_city_code, params=params_city_code)
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: Unexpected response format when retrieving airport code for {city}.")
            return "Not found"
        
        
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Searches for flight options between two cities on specified departure and return dates
        using the Amadeus API.
        Parameters:
            origin_city_code (str): The IATA code of the departure city.
            destination_city_code (str): The IATA code of the destination city.
            from_time (datetime): The departure date.
            to_time (datetime): The return date.
        Returns:
            dict or None: A dictionary containing flight offer data if the query is successful; None
            if there is an error.
        The function constructs a query with the flight search parameters and sends a GET request to
        the API. It handles the response, checking the status code and parsing the JSON data if the
        request is successful. If the response status code is not 200, it logs an error message and
        provides a link to the API documentation for status code details."""

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "EUR",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                "For details on status codes, check the API documentation:\n"
                "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                "-reference")
            print("Response body:", response.text)
            return None
        output = response.json()
        return output