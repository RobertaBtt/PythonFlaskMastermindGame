__author__ = 'roby'

class GameSession:

    def __init__(self):
        self.n_attempts = 0

    def get_game_id(self):
        return id(self)
