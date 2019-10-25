# Button class for Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

#import libraries
import pygame.font

class Button():
	
	def __init__(self, settings, screen, caption):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		# Build the buttons rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		# Prep the button caption
		self.prep_caption(caption)
		
	def prep_caption(self, caption):
		"""
		Turn the caption into a rendered image and center it on the
		button.
		"""
		self.caption_image = self.font.render(caption, True, 
								self.text_color, self.button_color)
		self.caption_image_rect = self.caption_image.get_rect()
		self.caption_image_rect.center = self.rect.center
		
	def draw_button(self):
		# Draw blank button thenoverlay the caption.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.caption_image, self.caption_image_rect)
