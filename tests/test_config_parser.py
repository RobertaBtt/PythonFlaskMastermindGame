__author__ = 'RobertaBtt'

import unittest
import configparser

class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.parser = configparser.ConfigParser()
        self.parser.read('config.ini')

    def test_config_url(self):
        url = self.parser.get('default', 'url')
        assert url == "http://localhost:"

    def test_config_port(self):
        port = self.parser.get('default', 'port')
        assert port == '5000'

    def test_config_balls(self):
        balls = self.parser.get('default', 'balls')
        assert balls == '3'

    def test_config_notfound(self):
        with self.assertRaises(Exception) as context:
            self.parser.get('default', 'notfound')

        self.assertEqual("No option 'notfound' in section: 'default'", context.exception.message)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
