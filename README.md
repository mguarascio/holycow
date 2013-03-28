holycow
=======
*A python wrapper for the ESPN (baseball) API*   
http://developer.espn.com/io-docs

Holy cow! (http://en.wikipedia.org/wiki/Phil_Rizzuto)

NOTE: Still a work-in-progress. Better exception handling to come...

Requirements
-----------------
- Python 2.6 to 2.7
- requests


Installation
------------
1) Install the required dependencies using your favorite installer (pip, easy_install)

2) Use Git to clone the repository from Github
and install it manually:

	git clone git@github.com:mguarascio/holycow.git
	python setup.py install

Examples
--------
	import holycow

	# initialize api
	api = holycow.API('your_api_key')

	# get all teams 
	teams = api.teams()
	print [team.name for team in teams]
        '''
            [u'Orioles', u'Red Sox', u'Angels', u'White Sox', u'Indians', u'Tigers', u'Royals', u'Brewers', u'Twins', u'Yankees', u'Athletics', u'Mariners', u'Rangers', u'Blue Jays', u'Braves', u'Cubs', u'Reds', u'Astros', u'Dodgers', u'Nationals', u'Mets', u'Phillies', u'Pirates', u'Cardinals', u'Padres', u'Giants', u'Rockies', u'Marlins', u'Diamondbacks', u'Rays']
	'''
 
	# get a specific team's data
	team = api.team(abbr='NYY')
	print ''.join([team.location, ' ', team.name, ': ', team.venue])
	# New York Yankees: Yankee Stadium 	

	# get all top news 
	topnews = api.news()
	print [news.headline for news in topnews]
	'''
	[u'Phillies 4, Tigers 1', u'Jason Hammel set to start opener', ... ]
	'''
	
	# get specific team's news
	news = api.team_news('NYY')
	print [story.links['web'] for story in news]	
	'''
	[{u'href': u'http://espn.go.com/new-york/mlb/story/_/id/9105109/phil-hughes-new-york-yankees-start-season-disabled-list?ex_cid=espnapi_public'}, {u'href': u'http://espn.go.com/mlb/story/_/id/9104778/forbes-mlb-teams-see-historic-23-percent-surge-average-values?ex_cid=espnapi_public'},...]
	'''

