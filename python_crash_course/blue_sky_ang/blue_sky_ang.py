# Blue Sky Ang
# Main Program
# 
# from Python Crash Course
# Part II Excercises
# by: Keith Kay
# October 2019

#import libraries
import pygame
from pygame.sprite import Group

#import from game modules
from settings import Settings
from hero import Hero
import game_functions as gf

def run_game():
	# Intialize the game and create the screen object
	pygame.init()
	gbs_settings = Settings()
	screen = pygame.display.set_mode(
		(gbs_settings.screen_width,
		 gbs_settings.screen_height))
	pygame.display.set_caption("Ang and the Great Blue Sky")
	
	# Add our hero and a group of fireballs
	hero = Hero(gbs_settings, screen)
	fireballs = Group()

	# Main game loop
	while True:
		gf.check_events(gbs_settings, screen, hero, fireballs)
		
		hero.update()
		gf.update_fireballs(screen, fireballs)

		gf.update_screen(gbs_settings, screen, hero, fireballs)
		
run_game()
