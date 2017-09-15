__author__ = 'robyb'

from flask import Flask
from flask import json

from flask import jsonify
from mastermind_config_parser import MastermindConfigParser
app = Flask(__name__)

@app.route("/")
def home():
    keys = ["balls", "colors", "attempts"]
    values = [MastermindConfigParser.get_balls(), MastermindConfigParser.get_colors(), MastermindConfigParser.get_attempts()]

    zipped_values = zip(keys, values)
    dictionary_values = dict(zipped_values)
    response = app.response_class(
        response=json.dumps(dictionary_values),
        status=200,
        mimetype='application/json'
    )


    return response



@app.route("/new/game")
def new_game():
    return "play"


