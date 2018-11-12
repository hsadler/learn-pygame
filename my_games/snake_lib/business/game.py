
# main game


class Game():

	def __init__(self, pygame, config, grid=None):
		self.config = config
		self.pygame = pygame
		self.pygame.init()
		self.pygame.display.set_caption("game template")
		self.screen = pygame.display.set_mode(
			(
				self.config.SCREEN_PX_WIDTH,
				self.config.SCREEN_PX_HEIGHT
			)
		)
		self.clock = pygame.time.Clock()
		self.running = True
		self.updated = []

	def run(self):
		"""
		game loop main method
		"""

		# exit event conditions
		for event in self.pygame.event.get():
			if event.type == self.pygame.QUIT:
				self.running = False
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_ESCAPE or event.unicode == 'q':
					self.running = False

		# block selection based on user input
		direction = self.get_direction_from_user_input()
		if direction is not None:
			print('direction:')
			print(direction)

		# lock game loop rate
		self.clock.tick(self.config.GAME_LOOP_RATE)

	def get_direction_from_user_input(self):
		return None

	def init_display(self):
		self.pygame.display.update()

	def update_display(self):
		# TODO: pass rects to update()
		self.pygame.display.update(rects)

	def clear_updated(self):
		self.updated = []

