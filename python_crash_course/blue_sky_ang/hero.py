# Blue Sky Ang
# Hero
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 2019

#import libraries
import pygame

class Hero():
	"""A class to define and manage the game's hero."""
	
	def __init__(self, settings, screen):
		"""Initialize and instance of Hero."""
		self.screen = screen
		self.settings = settings
		
		# Load the hero and get its rect.
		self.image = pygame.image.load('images/Aaing2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new hero in the center of the screen.
		self.rect.center = self.screen_rect.center
		
		# Store decimal values for our hero's center.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		# Set movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update our hero's position based on the movement flags."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.settings.hero_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.settings.hero_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.settings.hero_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.settings.hero_speed_factor
					
		# Update our hero's rect object's x and y
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
					
	def blitme(self):
		"""Draw our hero at its current location"""
		self.screen.blit(self.image, self.rect)
