#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program
# requirements.
from pprint import pprint
import time
from datetime import datetime, timedelta

from requests_cache import install_cache, DO_NOT_CACHE
from data_manager import DataManager
from flight_search import FlightSearch

# from flight_data import FlightData

install_cache('flight_cache', urls_expire_after={
    '*.sheety.co': DO_NOT_CACHE,
    '*': 3600})

ORIGIN_CITY_IATA = "AMS,EIN"
Tomorrow = datetime.now() + timedelta(days=1)
SixMonthsFromNow = (Tomorrow + timedelta(days=180))
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_data()
pprint(sheet_data)
# if sheet_data[0]["iataCode"] == "":
#     for line in sheet_data:
#         line["iataCode"] = flight_search.get_destination_code(line["city"])
#         time.sleep(2)

#     data_manager.update_sheet_data(sheet_data)



for line in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, line["iataCode"], Tomorrow, SixMonthsFromNow)
    flight_search.save_flight_data(flight)
    pprint(flight)
    time.sleep(2)