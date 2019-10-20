# Blue Sky Ang
# Settings
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 2019

class Settings():
	"""A class to store all the games settings."""
	
	def __init__(self):
		"""Initialize the games settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (15, 200, 240)
		
		# Hero settings
		self.hero_speed_factor = 2.2
