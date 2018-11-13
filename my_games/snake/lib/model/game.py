
# game model (holds global properties)


class Game():

	def __init__(self, config):
		self.config = config
		self.pygame = config.pygame
		self.screen = self.pygame.display.set_mode(
			(
				self.config.SCREEN_PX_WIDTH,
				self.config.SCREEN_PX_HEIGHT
			)
		)
		self.clock = self.pygame.time.Clock()
		self.running = True
		self.updated = []

	def get_running(self):
		return self.running
