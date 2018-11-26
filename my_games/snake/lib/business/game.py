
from lib.model.game import Game
from lib.model.grid import Grid
from lib.model.block import Block
from lib.model.snake import Snake
from lib.model.wall import Wall


# game business logic
	# - manages game object creation and initialization
	# - manages game logic
	# - manages user input


class GameBL():

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, game):
		self.game = game
		self.grid = None
		self.wall = None
		self.snake = None
		self.cur_direction = self.DIRECTION_LEFT
		self.game_over = False


	def init_new_game(self):

		config = self.game.config

		# initialize game
		self.game.initialize()

		# create grid
		self.grid = Grid(
			game=self.game,
			block_class=Block,
			block_size=(
				config.BLOCK_PX_WIDTH,
				config.BLOCK_PX_HEIGHT
			),
			block_color=config.NONE_BLOCK_COLOR,
			grid_dimensions=(
				config.GRID_WIDTH_BLOCKS,
				config.GRID_HEIGHT_BLOCKS
			)
		)
		self.grid.initialize()
		self.grid.update_all_blocks()

		# create wall
		grid_parimeter = self.grid.get_parimeter()
		self.wall = Wall(
			game=self.game,
			game_models=grid_parimeter,
			collidable=True,
			block_color=config.WALL_BLOCK_COLOR
		)
		self.grid.update_occupied_blocks(add=self.wall.get_game_models())
		self.wall.update()

		# create snake
		rand_grid_line = self.grid.get_random_line(config.SNAKE_START_LENGTH)
		self.snake = Snake(
			game=self.game,
			game_models=rand_grid_line,
			collidable=True,
			block_color=config.SNAKE_BLOCK_COLOR
		)
		self.grid.update_occupied_blocks(add=self.snake.get_game_models())
		self.snake.update()

		# initialize with entire display update
		self.game.init_display()


	def run_game_loop(self):
		"""
		game loop main method
		"""

		config = self.game.config

		# exit event conditions
		for event in self.game.pygame.event.get():
			if event.type == self.game.pygame.QUIT:
				self.game.set_restart(False)
				self.game.set_running(False)
				return False
			if event.type == self.game.pygame.KEYDOWN:
				if (
					event.key == self.game.pygame.K_ESCAPE or
					event.unicode == 'q'
				):
					self.game.set_restart(False)
					self.game.set_running(False)
					return False

		if self.game_over:
			self.game.set_running(False)
			return False

		# get current head
		head = self.snake.get_head()
		# get direction from user input or last direction
		direction = self.get_direction_from_user_input()
		direction = direction if direction is not None else self.cur_direction
		self.cur_direction = direction
		# get new snake head from user input direction
		new_head = None
		new_head = self.grid.get_adjacent_block_from_block(
			block=head,
			direction=direction
		)
		removed_tail_model = None
		if new_head is not None:
			# check for collision
			collision = self.grid.check_collision(
				add=[ new_head ],
				remove=[] # TODO: deal with tail removal later
			)
			if collision:
				self.game_over = True
				return False
			else:
				# move the snake
				removed_tail_model = self.snake.move_snake(
					new_head=new_head,
					remove_tail=True
				)

		# update occupied grid blocks
		to_add = []
		if new_head is not None:
			to_add.append(new_head)
		to_remove = []
		if removed_tail_model is not None:
			removed_tail_model.set_color(self.grid.get_block_color())
			removed_tail_model.draw()
			removed_tail_model.update()
			to_remove.append(removed_tail_model)
		self.grid.update_occupied_blocks(add=to_add, remove=to_remove)

		# do full update (until optimized)
		self.game.pygame.display.update()

		# lock game loop rate
		self.game.clock.tick(config.GAME_LOOP_RATE)


	def get_direction_from_user_input(self):
		pygame = self.game.pygame
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			return self.DIRECTION_UP
		elif pressed[pygame.K_RIGHT]:
			return self.DIRECTION_RIGHT
		elif pressed[pygame.K_LEFT]:
			return self.DIRECTION_LEFT
		elif pressed[pygame.K_DOWN]:
			return self.DIRECTION_DOWN
		return None

