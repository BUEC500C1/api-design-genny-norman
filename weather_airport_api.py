from flask import Flask, request
import requests

from airport_csv_functions import fetchLatLongFromIdent, fetchLatLongFromName

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homePage():
    return {'message':'Gennifer Norman Weather API'}

@app.route('/fetchCoordsFromIdent')
def fetchCoordsFromIdent():
    try:
        identVal = request.args.get('identVal', default="", type=str)
        lat, long = fetchLatLongFromIdent(identVal)
        return {
            "latitude": lat,
            "longitude": long
        }
    except:
        return {"error": "Invalid Request"}

@app.route('/fetchCoordsFromName')
def fetchCoordsFromName():
    try:
        name = request.args.get('name', default="", type=str)
        lat, long = fetchLatLongFromName(name)
        return {
            "latitude": lat,
            "longitude": long
        }
    except:
        return {"error": "Invalid Request"}

@app.route('/fetchWeather')
def fetchWeather():
    lat = request.args.get('lat', default="", type=str)
    long = request.args.get('long', default="", type=str)
    URL = "https://api.weather.gov/points/"+lat+","+long
    try:
        r = requests.get(URL)
        rJson = r.json()
        forecastURL = rJson['properties']['forecastHourly']
        r1 = requests.get(forecastURL)
        forecastJson = r1.json()
        return {
        "hourlyForecast": forecastJson['properties']['periods']
        }
    except:
        return {"error": "Invalid Request"}
