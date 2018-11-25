
# game business logic
	# - manages game logic
	# - manages user input


class GameBL():

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self):
		self.cur_direction = self.DIRECTION_LEFT
		self.game_over = False

	def run(self, config, game, grid, wall, snake):
		"""
		game loop main method
		"""

		# exit event conditions
		for event in game.pygame.event.get():
			if event.type == game.pygame.QUIT:
				game.running = False
			if event.type == game.pygame.KEYDOWN:
				if event.key == game.pygame.K_ESCAPE or event.unicode == 'q':
					game.running = False

		if self.game_over:
			return False

		# get current head
		head = snake.get_head()
		# get direction from user input or last direction
		direction = self.get_direction_from_user_input(game=game)
		direction = direction if direction is not None else self.cur_direction
		self.cur_direction = direction
		# get new snake head from user input direction
		new_head = None
		new_head = grid.get_adjacent_block_from_block(
			block=head,
			direction=direction
		)
		removed_tail_model = None
		if new_head is not None:
			# check for collision
			collision = grid.check_collision(
				add=[ new_head ],
				remove=[] # TODO: deal with tail removal later
			)
			if collision:
				self.game_over = True
				return False
			else:
				# move the snake
				removed_tail_model = snake.move_snake(
					new_head=new_head,
					remove_tail=True
				)

		# update occupied grid blocks
		to_add = []
		if new_head is not None:
			to_add.append(new_head)
		to_remove = []
		if removed_tail_model is not None:
			removed_tail_model.set_color(grid.get_block_color())
			removed_tail_model.draw()
			removed_tail_model.update()
			to_remove.append(removed_tail_model)
		grid.update_occupied_blocks(add=to_add, remove=to_remove)

		# do full update (until optimized)
		game.pygame.display.update()

		# lock game loop rate
		game.clock.tick(config.GAME_LOOP_RATE)

	@classmethod
	def get_direction_from_user_input(cls, game):
		pygame = game.pygame
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]:
			return cls.DIRECTION_UP
		elif pressed[pygame.K_RIGHT]:
			return cls.DIRECTION_RIGHT
		elif pressed[pygame.K_LEFT]:
			return cls.DIRECTION_LEFT
		elif pressed[pygame.K_DOWN]:
			return cls.DIRECTION_DOWN
		return None

