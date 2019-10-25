# Blue Sky Ang
# Game Functions
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 20199

# import libraries
import sys
import pygame

# import from other modules in this project
from fireball import Fireball

def check_keydown_events(event, settings, screen, hero, fireballs):
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
		shoot_fireball(settings, screen, hero, fireballs)
	elif event.key == pygame.K_q:
		sys.exit()
		
def shoot_fireball(settings, screen, hero, fireballs):
	"""Shoot a fireball from the hero if the limit has not been reached."""
	if len(fireballs) < settings.fireballs_allowed:
		new_fireball = Fireball(settings, screen, hero)
		fireballs.add(new_fireball)
	
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
		
def check_events(settings, screen, hero, fireballs):
	"""Respond to keypress and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, hero, fireballs)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, hero)
			
def update_screen(settings, screen, hero, fireballs):
	"""Update images on the screen flip to the new screen."""
	
	# Redraw the screen during each pass though the loop.
	
	# Background color
	screen.fill(settings.bg_color)
	
	# Redraw the hero and the fireballs
	fireballs.draw(screen)
	hero.blitme()
				
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	
def update_fireballs(screen, fireballs):
	"""
	Update the position of the fireballs and remove any that have
	gone off the screen.
	"""
	# Update positions
	fireballs.update()
	
	screen_rect = screen.get_rect()
	
	for fireball in fireballs.sprites():
		if fireball.rect.left >= screen_rect.right:
			fireballs.remove(fireball)
