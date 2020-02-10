import requests

def checkInput(sel):
    try:
        selInt = int(sel)
    except ValueError:
        print('input must be either 1 or 0')
        return "error"

    if selInt == 1 or selInt == 0:
        return selInt
    else:
        print('input must be either 1 or 0')
        return "error"

def prompt():
    print('\nHow would you like to search for an airport?')
    print('--------------------------------------------')
    print('0 - ident value')
    print('1 - airport name [must be exact]')
    print('--------------------------------------------')
    while True:
        inputType = input('Your selection: ')
        inputInt = checkInput(inputType)
        if inputInt != "error":
            break
    return inputInt

def saveCoordinates(coordJson):
    lat = coordJson['latitude']
    long = coordJson['longitude']
    return lat, long

def getCoordinates(requestType):
    if requestType == 0:
        identVal = input('Please enter the ident value of the airport: ')
        r = requests.get('http://localhost:5000/fetchCoordsFromIdent?identVal='+identVal)
        rJson = r.json()

    elif requestType == 1:
        airportName = input('Please enter the name of the airport: ')
        airportName.replace(' ','%20')
        r = requests.get('http://localhost:5000/fetchCoordsFromName?name='+airportName)
        rJson = r.json()

    lat, long = saveCoordinates(rJson)
    return lat, long

def getWeatherData(latitude, longitude):
    r = requests.get('http://localhost:5000/fetchWeather?lat='+str(latitude)+'&long='+str(longitude))
    rJson = r.json()
    return {'data': rJson}

def parseAndDisplayWeather(data):
    weatherData = data['data']['hourlyForecast']

    print('\n----------------HOURLY FORECAST----------------')
    for row in weatherData:
        print('\nFrom',row['startTime'],'to', row['endTime'], ': ')
        print('\t Summary:',row['shortForecast'])
        print('\t Temperature:', row['temperature'],row['temperatureUnit'])
        print('\t Wind:',row['windSpeed'],row['windDirection'])

def main_loop():
    inputType = prompt()
    lat, long = getCoordinates(inputType)
    print(lat, long)
    weatherData = getWeatherData(lat, long)
    parseAndDisplayWeather(weatherData)

if __name__ == '__main__':
    main_loop()
