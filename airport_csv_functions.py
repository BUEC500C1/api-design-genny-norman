import csv

def outputCsvContents():
    with open('airports.csv', newline='') as csvfile:
        fileReader = csv.reader(csvfile)
        return fileReader
