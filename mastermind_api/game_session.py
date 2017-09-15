__author__ = 'RobertaBtt'
from random import randint
from mastermind_api import mastermind_config_parser

class GameSession:

    def __init__(self):
        self.randoms = []
        self.n_attempts = 0
        self._create_game()

    def get_game_id(self):
        return id(self)

    def _create_game(self):
        """
        Create n numbers of random integers.
        Integers are from 1 to [colors]
        :return:
        """
        balls = mastermind_config_parser.MastermindConfigParser.get_balls()
        colors = mastermind_config_parser.MastermindConfigParser.get_colors()

        for x in xrange(int(balls)):

            new_int_random = randint(0,int(colors))
            self.randoms.append(new_int_random)

    def get_randoms(self):
        return self.randoms

    def add_attempt(self):
        self.n_attempts += self.n_attempts