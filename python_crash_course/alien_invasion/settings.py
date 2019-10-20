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
		self.ship_speed_factor = 5
		self.ship_limit = 3
		
		# Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 255, 165, 0
		self.bullets_allowed = 5
		
		# Alien settings
		self.alien_speed_factor = 80
		self.fleet_drop_speed = 10
		# fleet_direction of 1 means right; -1 means left
		self.fleet_direction = 1
		
		# Star settings
		self.star_speed_factor = 4.5
		self.star_width = 4
		self.star_height = 4
		self.star_color = [(255, 255, 255), (255,255,0)]
		self.min_star_distance = 100
