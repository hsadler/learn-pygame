
import pygame
import sys

import snake_lib.config as config
from snake_lib.game import Game
from snake_lib.block import Block
from snake_lib.grid import Grid
from snake_lib.snake import Snake


def main():

	# game
	game = Game(pygame=pygame, config=config)
	# grid
	grid = Grid(game=game)
	# initialize with entire display update
	game.pygame.display.update()

	# game loop
	while game.running:

		# exit event conditions
		for event in game.pygame.event.get():
			if event.type == game.pygame.QUIT:
				game.set_running(False)
			if event.type == game.pygame.KEYDOWN:
				if event.key == game.pygame.K_ESCAPE or event.unicode == 'q':
					game.set_running(False)

		# # block selection based on user input
		# direction = grid.get_direction_from_user_input()
		# if direction is not None:
		# 	new_selected_block = grid.get_adjacent_block_from_selected(
		# 		direction=direction
		# 	)
		# 	if new_selected_block:
		# 		grid.select_block(new_selected_block)

		# # update game objects
		# grid.update_selected()

		# # update display only selected block
		# pygame.display.update(grid.get_updated_rect())

		# # lock game loop rate
		# game_clock.tick(GAME_LOOP_RATE)


if __name__=="__main__":
	main()

