# A collection of functions for Alien Invasion
# from Python Crash Course
# includes exercise 14-1
# by: Eric Matthes
# adapted by: Keith Kay
# October 2019

#import libraries
import sys, pygame, json
from random import randint
from time import sleep

# import from other modules in this project
from bullet import Bullet
from alien import Alien
from star import Star

def check_keydown_events(event, settings, screen, stats, sb, play_button, 
							ship, aliens, bullets):
	"""Respond to key presses."""
	# Move right
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	# Move left
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	# Fire
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, stats, ship, bullets)
	# Play
	elif event.key == pygame.K_p:
		if not stats.game_active:
			start_game(settings, screen, stats, sb, play_button, ship,
						aliens, bullets)
	# Quit
	elif event.key == pygame.K_q:
		end_game(stats)
	# Pause
	elif event.key == pygame.K_ESCAPE:
		# Only pause if the game is active
		if stats.game_active == True:
			if stats.game_paused == True:
				stats.game_paused = False
			else:
				stats.game_paused = True
		
def fire_bullet(settings, screen, stats, ship, bullets):
	"""Fire a bullet if the limit has not been reached yet."""
	# Create a new bullet and add it to the bullets group.
	if stats.game_active and not stats.game_paused and len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)
	
def check_keyup_events(event, ship):
	"""Respond to key releases."""
	if event.key ==	pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False	

def check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets):
	"""Respond to keypress and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end_game(stats)
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, stats, sb,
									play_button, ship, aliens, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_mousedown_events(settings, screen, stats, sb, play_button,
									ship, aliens, bullets, mouse_x, mouse_y)
			
def check_mousedown_events(settings, screen, stats, sb, play_button, ship,
							aliens, bullets, mouse_x, mouse_y):
	"""Process MOUSEDOWN events appropriately."""
	
	# Play button
	play_button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if play_button_clicked and not stats.game_active:
		start_game(settings, screen, stats, sb, play_button, ship, aliens,
				bullets)

def start_game(settings, screen, stats, sb, play_button, ship, aliens,
				bullets):
	"""
	Start or restart the game if the player pressed "play" and reset 
	inital conditions.
	"""
	# Hide the mouse cursor.
	pygame.mouse.set_visible(False)
	
	# Reset game stats
	settings.initialize_dynamic_settings()
	stats.reset_stats()
	stats.game_active = True
	
	# Reset scoreboard
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	
	# Empty aliens and bullets
	aliens.empty()
	bullets.empty()	
	
	create_fleet(settings, screen, ship, aliens)
	ship.center_ship()

def end_game(stats):
	"""Write out the high score and exit the game."""
	stats.my_dict['high_score'] = stats.high_score
	with open(stats.filename, 'w') as file_obj:
		json.dump(stats.my_dict, file_obj)
		
	sys.exit()

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, 
			stars, play_button):
	"""Update images on the screen flip to the new screen."""
	
	# Redraw the screen during each pass though the loop.
	
	# Background color
	screen.fill(settings.bg_color)
	
	# Redraw all stars, then bullets, the ship and aliens.
	for star in stars.sprites():
		star.draw_star()

	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	aliens.draw(screen)
	
	sb.show_score()
			
	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
			
	# Make the most recently drawn screen visible.
	pygame.display.flip()

def check_bullet_alien_collision(settings, screen, stats, sb, ship, aliens, bullets):
	"""Respond to bullets that hit an alien."""
	# Check for any bullets that hit the aliens.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if collisions:
		for aliens in collisions.values():
			stats.score += settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
		
	# Check if we've destroyed the last alien, and if so re-populate the
	# fleet, speed up the game and increment the level
	if len(aliens) == 0:
		# Remove any remaining bullets
		bullets.empty()
		# Pause
		sleep(0.5)
		settings.increase_speed()
		
		# Level
		stats.level += 1
		sb.prep_level()
		
		create_fleet(settings, screen, ship, aliens)

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
	"""Update the position of the bullets and remove old bullets."""
	# Update bullet positions
	bullets.update()
		
	# Get rid of bullets that have passed the top of the screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
	check_bullet_alien_collision(settings, screen, stats, sb, ship, 
									aliens, bullets)
	
def get_number_alien_cols(settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = settings.screen_width - (2 * alien_width)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_alien_rows(settings, ship_height, alien_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (settings.screen_height - (3 * alien_height) -
							ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(settings, screen, aliens, col_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + (2 * alien_width * col_number)
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + (2 * alien.rect.height *
		row_number)
	aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	alien = Alien(settings, screen)
	number_aliens_cols = get_number_alien_cols(settings,
		alien.rect.width)
	number_alien_rows = get_number_alien_rows(settings,
		ship.rect.height,alien.rect.height)
	
	# Create the fleet of aliens.
	for row_number in range(number_alien_rows):
		for col_number in range(number_aliens_cols):
			create_alien(settings, screen, aliens, col_number,
				row_number)

def update_stars(settings, screen, stars):
	"""Update the position of the stars, remove and replace any stars
	that have left the screen."""
	# Update stars' positions
	stars.update()
		
	# Get rid of stars that have passed the bottom of the screen.
	for star in stars.copy():
		if star.rect.top >= settings.screen_height:
			stars.remove(star)
			
			# Generate a new star to replace it
			star = Star(settings, screen)
			star.rect.x = randint(0, settings.screen_width)
			star.rect.y = randint(0, settings.min_star_distance)
			star.y = float(star.rect.y)
			stars.add(star)


def create_starfield(settings, screen, stars):
	"""Populate a random field of stars into the Group stars."""
	# Determine the max number of stars that will fit in a row and cols
	max_stars_per_row = int(settings.screen_width / settings.min_star_distance)
	max_stars_per_col = int(settings.screen_height / settings.min_star_distance)
	
	# Generate a starfield with random placement
	for row_number in range(max_stars_per_row):
		for col_number in range(max_stars_per_col):
			star = Star(settings, screen)
			star.rect.x = int(row_number * settings.min_star_distance 
				+ (2 * settings.star_width)) + randint(-30,30)
			star.rect.y = int(col_number * settings.min_star_distance 
				+ (2 * settings.star_height)) + randint(-40,40)
			# Discard any stars that fall outside the screen
			if (star.rect.x >= 0 and
				star.rect.x <= settings.screen_width and
				star.rect.y >= 0 and
				star.rect.y <= settings.screen_height):
				star.y = float(star.rect.y)
				stars.add(star)

def change_fleet_direction(settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

def ship_hit(settings, screen, stats, sb, ship, aliens, bullets):
	"""Respond to the ship being hit by aliens."""
	
	if stats.ships_left > 0:
		# Decrement ships left
		stats.ships_left -= 1
		
		# Update scoreboard.
		sb.prep_ships()
		
		# Empty list of aliens and bullets
		aliens.empty()
		bullets.empty()
		
		# Create new fleet and center ship
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()
		
		# Pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		
def check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets):
	"""Check if any aliens have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit.
			ship_hit(settings, screen, stats, sb, ship, aliens, bullets)
			break
	
def update_aliens(settings, screen, stats, sb, ship, aliens, bullets):
	"""
	Check if the fleet is at an edge, and then update the positions of 
	all aliens in the fleet.
	"""
	check_fleet_edges(settings, aliens)
	aliens.update()
	
	# Look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, screen, stats, sb, ship, aliens, bullets)

	# Check if any aliens made it to the bottom.
	check_aliens_bottom(settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
	"""Check to see if there is a new high score."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
