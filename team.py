

'''
[{u'name': u'Red Sox', u'links': 
                        {u'mobile': {u'teams': {u'href': u'http://m.espn.go.com/mlb/clubhouse?teamId=2&ex_cid=espnapi_public'}}, 
                         u'web': {u'teams': {u'href': u'http://espn.go.com/mlb/team/_/name/bos/boston-red-sox?ex_cid=espnapi_public'}}, 
                         u'api': {u'news': {u'href': u'http://api.espn.com/v1/sports/baseball/mlb/teams/2/news'}, 
                                  u'notes': {u'href': u'http://api.espn.com/v1/sports/baseball/mlb/teams/2/news/notes'}, 
                                  u'teams': {u'href': u'http://api.espn.com/v1/sports/baseball/mlb/teams/2'}
                                  }
                         },
                         u'color': u'00314B', 
                         u'abbreviation': u'BOS', 
                         u'location': u'Boston', 
                         u'id': 2}]
'''


class Team():
    def __init__(self, results):
        self.id = results['id']
        self.name = results['name']
        self.color = results['color']
        self.abbreviation = results['abbreviation']
        self.location = results['location']
        self.links = results['links']
