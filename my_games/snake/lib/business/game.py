
# game business logic


class GameBL():

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	@classmethod
	def run(cls, config, game, grid, wall, snake):
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

		# update entire grid (until optimized)
		grid.update_all()

		# update entire wall (until optimized)
		wall.update()

		# move the snake
		head = snake.get_head()
		new_head = None
		direction = cls.get_direction_from_user_input(game=game)
		if direction is not None:
			new_head = grid.get_adjacent_block_from_block(
				block=head,
				direction=direction
			)
		if new_head is not None:
			snake.move_snake(new_head=new_head, remove_tail=True)
		snake.update()

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

	def init_display(self):
		self.pygame.display.update()

	def update_display(self, rects):
		# TODO: pass rects to update()
		self.pygame.display.update(rects)

	def clear_updated(self):
		self.updated = []

