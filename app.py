import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)


def get_co2():
    server = 'tcp:enviorment-server.database.windows.net'
    database = 'EnviormentDatabase'
    username = 'rokasbarasa1'
    password = 'Augis123*'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT top 1 * FROM [EnviormentDatabase].[dbo].[CarbonDioxideReading]')
    return dict(enumerate(item[0] for item in cursor))

def get_settings():
    server = 'tcp:enviorment-server.database.windows.net'
    database = 'EnviormentDatabase'
    username = 'rokasbarasa1'
    password = 'Augis123*'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM [EnviormentDatabase].[dbo].[Settings]')
    return dict(enumerate(item[0] for item in cursor))

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/co2', methods=['GET'])
def api_broiler_id():
    value = get_co2()
    print(value)
    return value

@app.route('/settings', methods=['GET'])
def api_live_co2():
    value = get_settings()
    print(value)
    return value

if __name__ == '__main__':
    app.run()
