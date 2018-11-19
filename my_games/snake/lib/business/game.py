
# game business logic


class GameBL():

	@staticmethod
	def run(config, game, grid, wall, snake):
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

		# update entire grid until optimized
		grid.initialize()

		# update entire wall until optimized
		wall.update()

		# move the snake
		head = snake.get_head()
		new_head = grid.get_adjacent_block_from_block(
			block=head,
			direction=grid.DIRECTION_LEFT
		)
		snake.move_snake(new_head=new_head, remove_tail=True)
		snake.update()

		# do full update (until optimized)
		game.pygame.display.update()

		# lock game loop rate
		game.clock.tick(config.GAME_LOOP_RATE)

	def get_direction_from_user_input(self):
		return None

	def init_display(self):
		self.pygame.display.update()

	def update_display(self, rects):
		# TODO: pass rects to update()
		self.pygame.display.update(rects)

	def clear_updated(self):
		self.updated = []

