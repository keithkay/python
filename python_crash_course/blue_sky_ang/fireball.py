# Blue Sky Ang
# Fireball
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 2019

#import libraries
import pygame
from pygame.sprite import Sprite

class Fireball(Sprite):
	"""A class to manage Aang's fireballs."""
	
	def __init__(self, settings, screen, hero):
		"""Create a fireball object at the hero's current postion."""
		super(Fireball, self).__init__()
		self.screen = screen
		self.settings = settings
		
		# Load the fireball and get its rect.
		self.image = pygame.image.load('images/aaing_fire.bmp')
		self.image = pygame.transform.rotozoom(self.image, 0, 
						self.settings.fireball_scaling_factor)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new alien near the top left of the screen, then
		# move it under our hero
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.rect.centery = hero.rect.centery
		self.rect.right = hero.rect.right
		
		# Store the fireball's position as a decimal value. We only need
		# the 'x' co-ord because the fireball will travel straight right
		# from the 'y' co-ord it is fired.
		self.x = float(self.rect.x)
		
		self.speed_factor = settings.fireball_speed_factor
		
	def update(self):
		"""Move the fireball right."""
		# Update the decimal 'x'co-ord
		self.x += self.speed_factor
		
		# Now use that to update the fireball's rect, which implictly
		# casts it to an INT
		self.rect.x = self.x

	def blitme(self):
		"""Draw the fireball at it's current location."""
		self.screen.blit(self.image, self.rect)
