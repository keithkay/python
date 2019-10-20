# Star class for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# Excerises 13-1, 13-2
# by: Keith Kay
# October 2019

import pygame
from pygame.sprite import Sprite
from random import randint, choice

class Star(Sprite):
	"""A class to manage the field of stars"""
	
	def __init__(self, settings, screen):
		"""Create a bullet object at the ship's current postion."""
		super(Star, self).__init__()
		self.screen = screen
		
		# Create a star rect at (0,0)
		self.rect = pygame.Rect(0, 0, settings.star_width,
			settings.star_height)
		
		# Store the star's position as a decimal value. We only need
		# the 'y' co-ord because the star will travel straight down from
		# the 'x' co-ord it is generated at.
		self.y = float(self.rect.y)
		
		self.color = choice(settings.star_color)
		self.speed_factor = settings.star_speed_factor + randint(-1,1)
		
	def update(self):
		"""Move the star down the screen."""
		# Update the decimal 'y'co-ord of the star.
		self.y += self.speed_factor
		
		# Now use that to update the star's rect, which implictly
		# casts it to an INT
		self.rect.y = self.y

	def draw_star(self):
		"""Draw the bullet on the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
