from flask import Flask, jsonify

from databaseAccess import DataAccess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/co2', methods=['GET'])
def api_broiler_id():
    value = DataAccess.get_co2()
    print(value)
    return value

@app.route('/settings', methods=['GET'])
def api_live_co2():
    value = DataAccess.get_settings()
    print(value)
    return value

if __name__ == '__main__':
    app.run()
