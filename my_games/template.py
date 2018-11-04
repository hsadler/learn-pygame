

import pygame


def main():

	# initialize the pygame module
	pygame.init()

	# set the caption at top of game window
	pygame.display.set_caption("game template")

	# create a surface on screen
	screen = pygame.display.set_mode((1000, 700))

	# game loop
	running = True
	while running:

		# event handling, gets all events from the eventqueue
		for event in pygame.event.get():

			# exit event conditions
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.unicode == 'q':
					running = False


if __name__=="__main__":
	main()
