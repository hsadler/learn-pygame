
# import the pygame module, so you can use it
import pygame


# define a main function
def main():

	# initialize the pygame module
	pygame.init()

	# set the caption at top of game window
	pygame.display.set_caption("game template")

	# create a surface on screen
	screen = pygame.display.set_mode((1000, 700))

	# define a variable to control the main loop
	running = True

	# main loop
	while running:

		# event handling, gets all events from the eventqueue
		for event in pygame.event.get():

			# exit event conditions
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.unicode == 'q':
					running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()
