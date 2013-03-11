

'''

The ESPN API currently only support getting all players, or player by id.
I'll have to implement a way to search by player's team or player name until
that API is available to the public.
'''


class Player():
    ''' Stub for player class '''
    def __init__(self, results):
        self.id = results['id']
        self.first_name = results['firstName']
        self.last_name = results['lastName']
        self.full_name = results['fullName']
        self.display_name = results['displayName']
        self.links = results['links']
