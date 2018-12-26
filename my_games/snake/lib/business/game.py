
from lib.model.game import Game
from lib.model.grid import Grid
from lib.model.block import Block
from lib.model.snake import Snake
from lib.model.food import Food
from lib.model.wall import Wall
from lib.model.points_display import PointsDisplay


# game business logic
	# - manages game object creation and initialization
	# - manages game logic
	# - manages user input


class GameBL():


	GAME_STATE_PLAY = 'gameame-state-play'
	GAME_STATE_CHECK_RESTART = 'game-state-check-restart'

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'


	def __init__(self, game):
		self.game = game
		self.grid = None
		self.wall = None
		self.snake = None
		self.food = None
		self.food_countdown = self.game.config.SNAKE_FOOD_COUNTDOWN
		self.cur_direction = self.DIRECTION_LEFT
		self.game_over = False
		self.game_state = self.GAME_STATE_PLAY


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
		grid_line = self.grid.get_center_horiz_line(config.SNAKE_START_LENGTH)
		self.snake = Snake(
			game=self.game,
			game_models=grid_line,
			collidable=True,
			block_color=config.SNAKE_BLOCK_COLOR
		)
		self.grid.update_occupied_blocks(add=self.snake.get_game_models())
		self.snake.update()

		# player points display
		self.points_display = PointsDisplay(
			game=self.game,
			x_pos=0,
			y_pos=0
		)

		# initialize with entire display update
		self.game.init_display()


	def run_game_loop(self):
		"""
		game loop main method
		"""

		config = self.game.config

		# exit event conditions
		if self.check_game_exit_conditions():
			return False

		# display dialoge if game is in 'check restart' state
		if self.game_state == self.GAME_STATE_CHECK_RESTART:
			self.check_restart()
			return False

		# create food block if needed
		self.try_create_food()

		# move snake
		new_head, removed_tail_model = self.move_snake()

		# check if snake ate food
		if self.food is not None and new_head == self.food.get_block():
			# feed snake, add point, and reset food properties
			self.snake.feed()
			self.points_display.increment_points()
			self.food = None
			self.food_countdown = config.SNAKE_FOOD_COUNTDOWN

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

		# update entire grid
		self.grid.update_all_blocks()

		# update points display
		self.points_display.draw()

		# do full update (until optimized)
		self.game.pygame.display.flip()

		# lock game loop rate
		self.game.clock.tick(config.GAME_LOOP_RATE)


	def check_game_exit_conditions(self):
		for event in self.game.pygame.event.get():
			if event.type == self.game.pygame.QUIT:
				self.game.set_restart(False)
				self.game.set_running(False)
				return True
			if event.type == self.game.pygame.KEYDOWN:
				if (
					event.key == self.game.pygame.K_ESCAPE or
					event.unicode == 'q'
				):
					self.game.set_restart(False)
					self.game.set_running(False)
					return True
		return False


	def try_create_food(self):
		if self.food is None:
			if self.food_countdown == 0:
				# create the food
				rand_block = self.grid.get_rand_avail_block()
				self.food = Food(
					game=self.game,
					game_model=rand_block,
					collidable=False,
					block_color=self.game.config.FOOD_BLOCK_COLOR
				)
				self.food.update()
			else:
				self.food_countdown -= 1


	def move_snake(self):
		# get current head
		head = self.snake.get_head()
		# get direction from user input or last direction
		direction = self.get_direction_from_user_input()
		# don't use direction if it cannot be used
		if (
			direction is None or
			self.is_direction_opposite(self.cur_direction, direction)
		):
			direction = self.cur_direction
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
				remove=[]
			)
			if collision:
				self.game_state = self.GAME_STATE_CHECK_RESTART
				return None, None
			else:
				# move the snake
				removed_tail_model = self.snake.move_snake(new_head=new_head)
		return new_head, removed_tail_model


	def check_restart(self):
		pygame = self.game.pygame
		config = self.game.config
		# get font
		font = pygame.font.Font(None, config.RESTART_TEXT_SIZE)
		# write score text
		score_text = 'Score: {0}'.format(
			self.points_display.get_points()
		)
		# size = font.size(score_text)
		text_width, text_height = font.size(score_text)
		ren = font.render(score_text, 0, config.RESTART_TEXT_COLOR)
		self.game.screen.blit(
			ren,
			(
				config.SCREEN_PX_WIDTH/2 - text_width/2,
				config.SCREEN_PX_HEIGHT/2 - text_height - text_height/2
			)
		)
		# write restart text
		restart_text = 'Press "R" to restart'
		# size = font.size(restart_text)
		text_width, text_height = font.size(restart_text)
		ren = font.render(restart_text, 0, config.RESTART_TEXT_COLOR)
		self.game.screen.blit(
			ren,
			(
				config.SCREEN_PX_WIDTH/2 - text_width/2,
				config.SCREEN_PX_HEIGHT/2 + text_height - text_height/2
			)
		)
		# check for 'r' key input
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_r]:
			self.game.set_running(False)
		self.game.pygame.display.flip()


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


	def is_direction_opposite(self, cur_direction, new_direction):
		opposite_map = {
			self.DIRECTION_UP: self.DIRECTION_DOWN,
			self.DIRECTION_DOWN: self.DIRECTION_UP,
			self.DIRECTION_RIGHT: self.DIRECTION_LEFT,
			self.DIRECTION_LEFT: self.DIRECTION_RIGHT
		}
		opposite = opposite_map[cur_direction]
		return opposite == new_direction


