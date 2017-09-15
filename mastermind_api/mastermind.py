__author__ = 'robyb'

from flask import Flask, json
from mastermind_config_parser import MastermindConfigParser
from game_sessions_proxy import GameSessionsProxy
from game_session import  GameSession

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

@app.route("/play/<gameid>/<code_string>")
def play_game(gameid, code_string=None):

    game_obj = GameSessionsProxy().get_game_by_id(gameid)

    if game_obj != None and code_string != '':
        game_obj.verify_code(code_string)

        response = app.response_class(
            response=['you are playing game:'+ gameid],
            status=200,
            mimetype='application/json'
        )
    elif game_obj != None and code_string == '':
        response = app.response_class(
            response=[],
            status=400,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=[],
            status=404,
            mimetype='application/json'
        )

    return response



