
import sys

from lib.model.config import Config
from lib.model.game import Game
from lib.model.grid import Grid
from lib.model.block import Block
from lib.model.snake import Snake
from lib.model.wall import Wall

from lib.business.game import GameBL


def main():

	# create config
	config = Config()

	# create stateful game manager
	game = Game(config=config)

	# create grid
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

	# create wall
	grid_parimeter = grid.get_parimeter()
	wall = Wall(game=game, game_models=grid_parimeter)
	wall.update()

	# create snake
	rand_grid_line = grid.get_random_line(config.SNAKE_START_LENGTH)
	snake = Snake(game=game, game_models=rand_grid_line)
	snake.update()

	# initialize with entire display update
	game.init_display()

	# game loop
	while game.get_running():
		GameBL.run(
			config=config,
			game=game,
			grid=grid,
			snake=snake
		)


if __name__=="__main__":
	main()

