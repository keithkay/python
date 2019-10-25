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
		
		# High score doesn't reset, load from a file
		self.load_saved_stats()
		print(self.high_score)
		
	def reset_stats(self):
		"""Initializes statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def load_saved_stats(self):
		"""Load stats from a file."""
		self.filename = 'ai_stats.json'
		self.my_dict = {}

		# first open the the file and determine if it is empty
		try:
			with open(self.filename, 'r') as file_obj:
				if file_obj.read():
					# The file is not empty
					print("I read something")
					# The seek(0) is need because the 'read()'above has moved the file
					# cursor to EOF, so we need to move it back
					file_obj.seek(0)
					self.my_dict = json.load(file_obj)
					self.high_score = int(self.my_dict['high_score'])
					print(self.high_score)
				else:
					# The file exists, but has nothing in it
					print("I read nothing")
					with open(self.filename, 'w') as file_obj:
						self.my_dict = {'high_score': '0'}
						json.dump(self.my_dict, file_obj)
					self.high_score = 0
					
		except FileNotFoundError:
			print("File doesn't exist")
			# Create the file and write the dict
			with open(self.filename, 'w') as file_obj:
				self.my_dict = {'high_score': '0'}
				json.dump(self.my_dict, file_obj)
			self.high_score = 0
				
		except KeyError:
			print("File exists, but key not found")
			# File exists but the key was not in the dict
			with open(self.filename, 'r+') as file_obj:
				self.my_dict = json.load(file_obj)
				file_obj.seek(0)
				file_obj.truncate()
				self.my_dict['high_score'] = '0'
				json.dump(self.my_dict, file_obj)
			self.high_score = 0
