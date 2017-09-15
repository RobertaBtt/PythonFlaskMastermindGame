__author__ = 'RobertaBtt'

from game_session import  GameSession

class GameSessionsProxy():
    class __GameSessionsProxy:
        def __init__(self):
            self.game_sessions = {}
        def __str__(self):
            return repr(self)
    instance = None
    def __init__(self):
        if not GameSessionsProxy.instance:
            GameSessionsProxy.instance = GameSessionsProxy.__GameSessionsProxy()

    def __getattr__(self, name):
        return  getattr(self.instance, name)


    def create_game(self):
        """
        Create and store the new game into a dictionary
        :return:
        """
        new_game_session = GameSession()
        self.game_sessions[id(new_game_session)] = new_game_session
        return id(new_game_session)

    def get_game_sessions(self):
        return self.game_sessions

    def get_game_by_id(self, instance_id):
        try:
            return self.game_sessions[int(instance_id)]
        except KeyError:
            return None