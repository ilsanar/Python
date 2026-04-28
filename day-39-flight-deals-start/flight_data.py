class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
    
    pass