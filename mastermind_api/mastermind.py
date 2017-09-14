__author__ = 'robyb'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"


@app.route("/new/game")
def new_game():
    return "play"


