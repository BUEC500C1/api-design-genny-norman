import csv

def fetchLatLongFromIdent(identVal):
    try:
        with open('airports.csv', newline='') as csvfile:
            fileReader = csv.reader(csvfile)
            for row in fileReader:
                    if row[1] == identVal:
                        return row[4], row[5] #return lat, long
    except:
        return "ERROR: coordinates not found"

def fetchLatLongFromName(name):
    try:
        with open('airports.csv', newline='') as csvfile:
            fileReader = csv.reader(csvfile)
            for row in fileReader:
                if row[3] == name:
                    return row[4], row[5]
    except:
        return "ERROR: coordinates not found"
