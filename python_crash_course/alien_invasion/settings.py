# Settings for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

class Settings():
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		
		#Screen settings
		self.screen_width = 1400
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		
		# Ship settings
		self.ship_limit = 3
		
		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 165, 0
		self.bullets_allowed = 5
		
		# Alien settings
		self.fleet_drop_speed = 10
		self.alien_scaling_factor = 0.95
		
		# Star settings
		self.star_speed_factor = 4.5
		self.star_width = 4
		self.star_height = 4
		self.star_color = [(255, 255, 255), (255,255,0)]
		self.min_star_distance = 100

		# Game speed settings
		self.speedup_scale = 1.2
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		# Speed factors
		self.ship_speed_factor = 8
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 3

		# Fleet_direction of 1 means right; -1 means left
		self.fleet_direction = 1
		
		# Scoring
		self.alien_points = 50
		
	def increase_speed(self):
		"""Increase speed settings and alient point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
