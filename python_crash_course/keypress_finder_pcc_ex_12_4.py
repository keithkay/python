# Python Crash Course
#
# Chapter 12 - Game development
#
# Keypress finder exercise 12-4

#import libraries
import pygame

def run_game():
	# Intialize the game and create the screen object
	pygame.init()
	
	# Screen settings
	screen_width = 600
	screen_height = 400
	bg_color = (230, 230, 230)
	
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Press any Key")
	
	# Main game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(event.key)

		# Redraw the screen during each pass though the loop.
		screen.fill(bg_color)
				
		# Make the most recently drawn screen visible.
		pygame.display.flip()
		
run_game()
