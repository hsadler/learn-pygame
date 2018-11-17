
# game business logic


class GameBL():

	@staticmethod
	def run(config, game, grid, snake):
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

		# # block selection based on user input
		# direction = self.get_direction_from_user_input()
		# if direction is not None:
		# 	print('direction:')
		# 	print(direction)

		# # lock game loop rate
		# self.clock.tick(self.config.GAME_LOOP_RATE)

	def get_direction_from_user_input(self):
		return None

	def init_display(self):
		self.pygame.display.update()

	def update_display(self):
		# TODO: pass rects to update()
		self.pygame.display.update(rects)

	def clear_updated(self):
		self.updated = []

