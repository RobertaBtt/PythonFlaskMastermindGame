__author__ = 'RobertaBtt'

import unittest
from ..mastermind_api import mastermind_config_parser


class TestMastermindConfigParser(unittest.TestCase):

    def test_get_config_balls(self):
        balls = mastermind_config_parser.MastermindConfigParser._get_value('balls')
        assert balls == "4"

    def test_get_config_colors(self):
        colors = mastermind_config_parser.MastermindConfigParser._get_value('colors')
        assert colors == "9"

    def test_get_config_attempts(self):
        attempts = mastermind_config_parser.MastermindConfigParser._get_value('attempts')
        assert attempts == "10"

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()