__author__ = 'robyb'

import unittest
from ConfigParser import SafeConfigParser

class MastermindAPITestConfigCase(unittest.TestCase):

    def setUp(self):
        self.parser = SafeConfigParser()
        self.parser.read('config.ini')

    def test_config_url(self):
        url = self.parser.get('default', 'url')
        assert url == "http://localhost:"

    def test_config_port(self):
        port = self.parser.get('default', 'port')
        assert port == '5000'

    def test_config_balls(self):
        balls = self.parser.get('default', 'balls')
        assert balls == '4'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()