# Alien Invasion
# from Python Crash Course
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

#import libraries
import pygame
from pygame.sprite import Group

# import from other files in this project
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize game and create settings, stats,  and screen objects.
	pygame.init()
	ai_settings = Settings()
	stats = GameStats(ai_settings)
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Make a ship, a group of bullets, a group of aliens, and a
	# starfield.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stars = Group()

	# Create a fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Create the initial starfield.
	gf.create_starfield(ai_settings, screen, stars)
	
	# Start the main game loop.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		gf.update_stars(ai_settings, screen, stars)
		
		if stats.game_active and stats.game_pause == False:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, ship, aliens, bullets, 
			stars)		

# main function call
run_game()
