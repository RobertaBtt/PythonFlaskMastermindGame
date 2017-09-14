__author__ = 'robyb'

import unittest
from mastermind_api import mastermind

class MastermindAPITestCase(unittest.TestCase):

    def setUp(self):
        app = mastermind.app
        app.config['TESTING'] = True
        self.baseURL = "http://localhost:5000"
        self.client = app.test_client()

        return app


    def test_get_home(self):
        rv = self.client.get('/')
        assert rv.status_code == 200

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()