__author__ = 'robyb'

import unittest
from mastermind_api import mastermind
from mastermind_api import game_sessions_proxy
import json

class TestMastermindAPI(unittest.TestCase):

    def setUp(self):
        app = mastermind.app
        app.config['TESTING'] = True
        self.baseURL = "http://localhost:5000"
        self.client = app.test_client()

        #Test the game retrieving the game with the singleton proxy
        self.game_sessions_proxy = game_sessions_proxy.GameSessionsProxy()

        return app

    def test_get_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_get_home_get_balls_config(self):
        response = self.client.get('/')
        assert json.loads(response.data)['balls'] == '4'

    def test_new_game(self):
        response = self.client.get('new/game')
        assert response.status_code == 200

    def test_new_game_created(self):
        response = self.client.get('new/game')
        assert json.loads(response.data)['id'] != None

    def test_play_existing_game_no_code(self):
        response_new_game = self.client.get('new/game')
        game_id = json.loads(response_new_game.data)['id']
        response = self.client.get('play/'+str(game_id))
        assert 301 == response._status_code

    def test_play_not_existing_game(self):
        response = self.client.get('play/'+str(999999))
        assert 301 == response._status_code

    def test_play_with_code(self):
        response_new_game = self.client.get('new/game')
        game_id = json.loads(response_new_game.data)['id']
        random = self.game_sessions_proxy.get_game_by_id(game_id).get_randoms()

        response = self.client.get('play/'+str(game_id)+'/3,8,3,2')
        assert 200 == response._status_code


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()