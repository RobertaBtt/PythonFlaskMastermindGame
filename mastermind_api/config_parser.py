__author__ = 'roby'

from ConfigParser import SafeConfigParser
import logging

_logger = logging.getLogger(__name__)

class MastermindConfigParser:

    @staticmethod
    def get_balls():
        try:
            parser = SafeConfigParser()
            parser.read('../config.ini')
            balls = parser.get('default', 'balls')
            return balls

        except Exception as e:
            _logger.info(str(e))

    @staticmethod
    def get_colors():
        try:
            parser = SafeConfigParser()
            parser.read('../config.ini')
            colors = parser.get('default', 'colors')
            return colors

        except Exception as e:
            _logger.info(str(e))

    @staticmethod
    def get_attempts():
        try:
            parser = SafeConfigParser()
            parser.read('../config.ini')
            attempts = parser.get('default', 'attempts')
            return attempts

        except Exception as e:
            _logger.info(str(e))




MastermindConfigParser().get_balls()