
import sys

from lib.model.config import Config
from lib.model.game import Game
from lib.model.grid import Grid
from lib.model.block import Block
from lib.model.snake import Snake

from lib.business.game import GameBL


def main():

	# create config
	config = Config()

	# create stateful game manager
	game = Game(config=config)

	# create game objects
	grid = Grid(
		game=game,
		block_class=Block,
		block_size=(
			config.BLOCK_PX_WIDTH,
			config.BLOCK_PX_HEIGHT
		),
		grid_dimensions=(
			config.GRID_WIDTH_BLOCKS,
			config.GRID_HEIGHT_BLOCKS
		)
	)
	grid.initialize()

	rand_grid_line = grid.get_random_line(5)
	snake = Snake(game=game, game_models=rand_grid_line)
	snake.update()

	# initialize with entire display update
	game.init_display()

	# game loop
	while game.get_running():
		GameBL.run(config=config, game=game)


if __name__=="__main__":
	main()

