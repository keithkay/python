# Game Stats class for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

class GameStats():
	"""A class to track statistics for Alien Invasion"""
	
	def __init__(self, settings):
		"""Initialize statistics."""
		self.settings = settings
		self.reset_stats()
		
		# Start in an active state
		self.game_active = True
		self.game_paused = False
		
	def reset_stats(self):
		"""Initializes statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
