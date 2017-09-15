__author__ = 'robyb'

from flask import Flask, json
from mastermind_config_parser import MastermindConfigParser
from game_sessions_proxy import GameSessionsProxy

app = Flask(__name__)

@app.route("/")
def home():
    keys = ["balls", "colors", "attempts"]
    values = [MastermindConfigParser.get_balls(),
             MastermindConfigParser.get_colors(),
             MastermindConfigParser.get_attempts()]

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
    new_game_id = GameSessionsProxy().create_game()

    dictionary_values = {'id': new_game_id}

    response = app.response_class(
        response=json.dumps(dictionary_values),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/play/<gameid>")
def play_game(gameid):
    game_obj = GameSessionsProxy().get_game_by_id(gameid)
    if game_obj != None:
        response = app.response_class(
            response=[],
            status=200,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=[],
            status=404,
            mimetype='application/json'
        )

    return response



