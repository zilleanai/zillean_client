from .data import Data

class Project(object):
    def __init__(self, apihost, name, api='/api/v1'):
        self.apihost = apihost
        self.name = name
        self.api = api

    def api_root(self):
        return self.apihost + self.api

    def get_data(self):
        return Data(self)