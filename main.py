import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

broiler = [
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

]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/products', methods=['GET'])
def api_all():
    response = jsonify(broiler[0])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
app.run()