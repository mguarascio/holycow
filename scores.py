

class EventScore():
    ''' Only available via partner api. Very much a WIP for @baseballhackday....
        (aka, it's ugly)
    '''
    def __init__(self, results):
        self.id = results['id']
        self.date = results['date']
        self.competitors = results['competitors']
        self.score = dict([(competitor['team']['name'], competitor['score']) for competitor in self.competitors])
        self.inning = results['period']
        self.status = results['status']['detail']

    def latest_score(self):
        return self.score
