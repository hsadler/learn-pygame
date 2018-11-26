
# game model
	# - holds global game properties


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
		self.restart = True
		self.updated = []

	def initialize(self):
		self.running = True
		self.restart = True

	def get_running(self):
		return self.running

	def set_running(self, val):
		self.running = val

	def get_restart(self):
		return self.restart

	def set_restart(self, val):
		self.restart = val

	def init_display(self):
		self.pygame.display.update()
