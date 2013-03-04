import requests
import json
from team import Team


class API(object):
    def __init__(self, api_key,
                       urlroot='http://api.espn.com',
                       version='v1',
                       api_root='sports/baseball/mlb'
                       ):
        self.api_key = api_key
        self.urlroot = urlroot
        self.version = version
        self.api_root = api_root

    def team(self, teamid):
        method = ''.join(['teams/', teamid])
        response = self.__request(method)
        return Team(response['teams'][0])

    def teams(self):
        method = 'teams'
        return self.__request(method)

    def __request(self, method):
        url = ''.join([self.urlroot, '/',
                       self.version, '/',
                       self.api_root, '/',
                       method,
                       '?apikey=', self.api_key])

        r = requests.get(url)
        response = json.loads(r.text)
        league = response['sports'][0]['leagues'][0]
        return league
