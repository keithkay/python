# Bullet class for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""
	
	def __init__(self, settings, screen, ship):
		"""Create a bullet object at the ship's current postion."""
		super(Bullet, self).__init__()
		self.screen = screen
		
		# Create a bullet rect at (0,0) and then set the correct
		# position.
		self.rect = pygame.Rect(0, 0, settings.bullet_width,
			settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Store the bullet's position as a decimal value. We only need
		# the 'y' co-ord because the bullet will travel straight up from
		# the 'x' co-ord it is fired.
		self.y = float(self.rect.y)
		
		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor
		
	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal 'y'co-ord of the bullet.
		self.y -= self.speed_factor
		
		# Now use that to update the bullet's rect, which implictly
		# casts it to an INT
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet on the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
