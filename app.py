import numpy as np
from flask import Flask, request, jsonify
app = Flask(__name__)

broilers = [
    {
        'id': 1,
        'title': 'Bbq chicken wings',
        'co2': 23,
        'distance': 233,
        'water': 21,
        'manufacturer': 'Rose',
        'energy': 499,
        'description': 'Sitas sudas yra padarytas kazkada labai senei ir niekas jo nepirko. Dazniausiai randamas siukslinese.',
    },
    {
        'id': 2,
        'title': 'Bbq chicken wings',
        'co2': 23,
        'distance': 233,
        'water': 21,
        'manufacturer': 'Rose',
        'energy': 499,
        'description': 'Sitas sudas yra padarytas kazkada labai senei ir niekas jo nepirko. Dazniausiai randamas siukslinese.',
    },
    {
        'id': 3,
        'title': 'Bbq chicken wings',
        'co2': 23,
        'distance': 233,
        'water': 21,
        'manufacturer': 'Rose',
        'energy': 499,
        'description': 'Sitas sudas yra padarytas kazkada labai senei ir niekas jo nepirko. Dazniausiai randamas siukslinese.',
    },

]

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/broilers', methods=['GET'])
def api_all():
    response = jsonify(broilers)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/broilers/id', methods=['GET'])
def api_broiler_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for broiler in broilers:
        if broiler['id'] == id:
            results.append(broiler)
    return jsonify(results)

@app.route('/getLiveCO2', methods=['GET'])
def api_live_co2():
    co2 = numpy.random.random_integers(410, 3000)
    return jsonify(co2)

if __name__ == '__main__':
    app.run()
