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


@app.route("/play/<gameid>/")
def play_game_no_code(gameid, code_string=None):
    response = app.response_class(
            response=['please give me the numbers you want to play'],
            status=400,
            mimetype='application/json'
        )
    return response

@app.route("/play/<gameid>/<code_string>")
def play_game(gameid, code_string=None):

    game_obj = GameSessionsProxy().get_game_by_id(gameid)

    if game_obj != None and code_string != '':
        game_result = game_obj.verify_code(code_string)
        response = app.response_class(
            response=json.dumps(game_result),
            status=200,
            mimetype='application/json'
        )
        print response
    elif game_obj != None and code_string == '':
        response = app.response_class(
            response=['please give me a code'],
            status=400,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=['game not found'],
            status=404,
            mimetype='application/json'
        )

    return response


@app.errorhandler(404)
def page_not_found(e):
    response = app.response_class(
            response=['not found'],
            status=404,
            mimetype='application/json'
        )
    return response




