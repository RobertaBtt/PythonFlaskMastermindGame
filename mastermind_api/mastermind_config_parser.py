__author__ = 'roby'

from ConfigParser import SafeConfigParser
import logging

_logger = logging.getLogger(__name__)

class MastermindConfigParser:

    @staticmethod
    def get_balls():
        try:
            balls = MastermindConfigParser._get_value('balls')
            return balls

        except Exception as e:
            _logger.info(str(e))
            return 0

    @staticmethod
    def get_colors():
        try:
            colors = MastermindConfigParser._get_value('colors')
            return colors

        except Exception as e:
            _logger.info(str(e))
            return []

    @staticmethod
    def get_attempts():
        try:
            attempts = MastermindConfigParser._get_value('attempts')
            return attempts

        except Exception as e:
            _logger.info(str(e))
            return 0

    @staticmethod
    def _get_value(key):
        try:
            section = 'default'
            parser = SafeConfigParser()
            parser.read('config.ini')

            value = parser.get(section, key)
            return value

        except Exception as e:
            print e
            if e.message == 'No section: \''+section+'\'':
                raise KeyError
            elif e.message == 'No option \''+key+'\' in section: \''+section+'\'':
                raise Exception



MastermindConfigParser().get_balls()