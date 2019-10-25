# GameStats class for Alien Invasion
# from Python Crash Course
# includes exercise 14-4
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

#import libraries
import json

class GameStats():
	"""A class to track statistics for Alien Invasion"""
	
	def __init__(self, settings):
		"""Initialize statistics."""
		self.settings = settings
		self.stats_data = {}
		self.reset_stats()
		
		# Start in an in-active state
		self.game_active = False
		self.game_paused = False

		# Read the high score, or create the json file if missing
		# ~ try:
			# ~ filename = 'ai_data.json'
			# ~ with open(filename, 'r+') as file_obj:
				# ~ first_char = file_obj.read(1)
				# ~ if first_char: 
					# ~ stat_data = json.load(file_obj)
					# ~ for element in stat_data:
						# ~ print(element)
						# ~ if element == 'highscore':
							# ~ self.high_score = int(element['highscore'])
				# ~ else:
					# ~ # File is empty, create file
					# ~ initial_highscore_str = {'highscore': '0'}
					# ~ json.dump(initial_highscore_str, file_obj)
					# ~ self.high_score = 0
		# ~ except NameError:
			# ~ pass
		
		# High score doesn't reset.
		self.high_score = 0
		
	def reset_stats(self):
		"""Initializes statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
