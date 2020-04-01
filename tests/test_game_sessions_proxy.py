__author__ = 'RobertaBtt'

import unittest
from ..mastermind_api import game_sessions_proxy

class TestGameSessionsProxy(unittest.TestCase):

    def setUp(self):
        self.game_sessions_proxy = game_sessions_proxy.GameSessionsProxy()
        self.game_sessions_proxy2 = game_sessions_proxy.GameSessionsProxy()

    def test_create_game(self):
        new_game_id = self.game_sessions_proxy.create_game()
        assert new_game_id != None

    def test_create_two_games(self):
        new_game_id = self.game_sessions_proxy.create_game()
        new_game_id2= self.game_sessions_proxy.create_game()
        assert new_game_id != new_game_id2

    def test_create_and_retrieve(self):
        new_game_id = self.game_sessions_proxy .create_game()
        new_game_obj = self.game_sessions_proxy.get_game_by_id(new_game_id)
        assert new_game_obj != None
        assert new_game_id == id(new_game_obj)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()