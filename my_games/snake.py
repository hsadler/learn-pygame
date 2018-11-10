

import pygame
import random
import sys


GAME_LOOP_RATE = 30

SCREEN_PX_WIDTH = 1000
SCREEN_PX_HEIGHT = 700


from snake_lib.game import Game
from snake_lib.block import Block
from snake_lib.grid import Grid
from snake_lib.snake import Snake


BG_COLOR = pygame.Color('black')

BLOCK_PX_WIDTH = 10
BLOCK_PX_HEIGHT = 10
BLOCK_COLOR = pygame.Color('gray30')
BLOCK_SELECTED_COLOR = pygame.Color('green')
BLOCK_STROKE_COLOR = pygame.Color('black')
BLOCK_STROKE_PX_WIDTH = 1

GRID_WIDTH_BLOCKS = int(SCREEN_PX_WIDTH / BLOCK_PX_WIDTH)
GRID_HEIGHT_BLOCKS = int(SCREEN_PX_HEIGHT / BLOCK_PX_HEIGHT)


def main():

	# initialize the pygame module
	pygame.init()
	# set the caption at top of game window
	pygame.display.set_caption("game template")
	# create a surface on screen
	screen = pygame.display.set_mode((SCREEN_PX_WIDTH, SCREEN_PX_HEIGHT))
	# get instance of the game clock
	game_clock = pygame.time.Clock()

	# grid
	grid = Grid(
		pygame=pygame,
		screen=screen,
		width=GRID_WIDTH_BLOCKS,
		height=GRID_HEIGHT_BLOCKS,
		block_size=(BLOCK_PX_WIDTH, BLOCK_PX_HEIGHT)
	)
	# set random block as selected
	grid.select_random_block()
	# update all the blocks in the grid as initialization step
	grid.update()

	# initialize with entire display update
	pygame.display.update()

	# game loop
	running = True
	while running:

		# exit event conditions
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.unicode == 'q':
					running = False

		# block selection based on user input
		direction = grid.get_direction_from_user_input()
		if direction is not None:
			new_selected_block = grid.get_adjacent_block_from_selected(
				direction=direction
			)
			if new_selected_block:
				grid.select_block(new_selected_block)

		# update game objects
		grid.update_selected()

		# update display only selected block
		pygame.display.update(grid.get_updated_rect())

		# lock game loop rate
		game_clock.tick(GAME_LOOP_RATE)


if __name__=="__main__":
	main()

