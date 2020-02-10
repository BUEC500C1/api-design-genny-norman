from flask import Flask
from airport_csv_functions import outputCsvContents

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homePage():
    return 'Gennifer Norman Weather API'
