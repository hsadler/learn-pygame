
import sys

from lib.model.config import Config
from lib.model.game import Game
# from lib.block import Block
# from lib.grid import Grid
# from lib.snake import Snake

from lib.business.game_logic import GameBL


def main():

	# create config
	config = Config()

	# create stateful game manager
	game = Game(config=config)

	# create game objects
	# grid = Grid(game=game)

	# instantiate game manager
	# game = Game(pygame=pygame, config=config)
	# initialize with entire display update
	# game.init_display()

	# game loop
	while game.get_running():
		GameBL.run(config=config, game=game)


if __name__=="__main__":
	main()

