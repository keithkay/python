# Blue Sky Ang
# Game Functions
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 20199

import sys
import pygame

def check_keydown_events(event, hero):
	"""Respond to key presses."""
	if event.key == pygame.K_RIGHT:
		hero.moving_right = True
	elif event.key == pygame.K_LEFT:
		hero.moving_left = True
	elif event.key == pygame.K_UP:
		hero.moving_up = True
	elif event.key == pygame.K_DOWN:
		hero.moving_down = True
	elif event.key == pygame.K_SPACE:
		# to-do fireball logic
		continue
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, hero):
	"""Respond to key releases."""
	if event.key ==	pygame.K_RIGHT:
		hero.moving_right = False
	elif event.key == pygame.K_LEFT:
		hero.moving_left = False	
	elif event.key == pygame.K_UP:
		hero.moving_up = False
	elif event.key == pygame.K_DOWN:
		hero.moving_down = False
		
def check_events(hero):
	"""Respond to keypress and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, hero)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, hero)
			
def update_screen(settings, screen, hero):
	"""Update images on the screen flip to the new screen."""
	
	# Redraw the screen during each pass though the loop.
	screen.fill(settings.bg_color)
	hero.blitme()
				
	# Make the most recently drawn screen visible.
	pygame.display.flip()
