# Airport Weather API

## Summary
- Make use of nested API calls (using weather.gov)
- Develop API that takes in information about an airport and returns relevant weather statistics
  - Input: ident value or airport name
  - Output: hourly forecast and summary for the next week at the given airport
- Integrate unit testing and CI/CB

## Using the API

The flask app runs on ```http://localhost:5000``` which hosts the endpoints for the API. The available endpoints are as follows:

1. ```/``` : returns a welcome message and requires no parameters
2. ```/fetchCoordsFromName``` : returns the latitude and longitude of an airport given the airport's name. Requires a valid airport name (checked against _airports.csv_)
3. ```/fetchCoordsFromIdent``` : returns the latitude and longitude of an airport given the airport's ident value. Requires a valid ident value (checked against _airports.csv_)
4. ```/fetchWeather``` : returns an extensive weather summary from the open weather.gov API. Requires the latitude and longitude of desired location

## Dependencies

- flask: micro web framework for running python applications
- requests: HTTP library for making requests

## Running the Code

- Please install the above dependencies
- Clone this repository and navigate in terminal to the root directory
- Run ```flask run```
- In another terminal window run ```py airport_weather_script.py``` to run the example module to interface with the API
