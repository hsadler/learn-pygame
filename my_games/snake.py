
import pygame
import sys

import snake_lib.config as config
from snake_lib.game import Game
from snake_lib.block import Block
from snake_lib.grid import Grid
from snake_lib.snake import Snake


def main():

	# instantiate game objects
	grid = Grid(game=game)

	# instantiate game manager
	game = Game(pygame=pygame, config=config)
	# initialize with entire display update
	game.init_display()

	# game loop
	while game.running:
		game.run()


if __name__=="__main__":
	main()

