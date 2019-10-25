# Ship class for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

#import libraries
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Defines the class for the player's ship"""
	
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		super(Ship, self).__init__()
		self.screen = screen
		self.settings = ai_settings
		
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		
		# Define the movement flags.
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.ship_speed_factor
		
		# Update the rect object from self.center, this allows us to
		# have decimal values for 'ship_speed_factor' as centerx only
		# takes integers
		self.rect.centerx = self.center
	
	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
