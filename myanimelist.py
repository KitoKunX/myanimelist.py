#############################
# MyAnimeList Data Module
# Author: Kitokunx
# Version: 0.7 (Incomplete)
# Contact: kitokunxd@gmail.com
#############################

import requests

class MAL(object):

	'''
	Main MyAnimeList object with search functions and data required.
	Required Properties:
		- username :: e.g. self.username = "KitoKunX"
		- password :: e.g. self.password = "passwordhere"
	Given Properties:
		- Search Url :: _search_url
	Functions:
		- Auth Confirmation :: confirm_auth
		- Anime/Manga search :: search :: Arguements =  query, type (anime/manga)
	'''
	 
	 def __init__(self):
		self._username = ""
		self._password = ""
		self._search_url = "http://myanimelist.net/api/%s/search.xml"
		self._auth_object = self.confirm_auth()
		
	def confirm_auth(self):
		c_auth = requests.get('http://myanimelist.net/api/account/verify_credentials.xml', auth = (self.username, self.password))
		return c_auth
		
	def search(self, query, type):
		data = {"q":args}
		_search_url = self._search_url
		_search_url = _search_url % (type)
		c_obj = requsts.get(
				_search_url,
				auth = (self.username, self.password),
				headers = {},
				timeout = 30
		)
		return
		#create object for each type
		
							
		
		
class Anime(object):

	'''
	Anime object for MyAnimeList.
	Required Class:
		- MAL
	Given Properties:
		- Title
		- Synonyms
		- Episodes
		- Synopsis
		- Air Date
		- Few other information
	Functions:
		- Linked with MAL object
	'''
	
	def __init__(self):
		self.title = ""
		self.synonyms = ""
		self.episodes = ""
		self.synopsis = ""
		self.air_data = ""
		
	def set_properties(*args):
		return
		
