
# main game


class Game():

	def __init__(self, pygame, config):
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

	def update_display(self):
		# TODO: pass rects to update()
		self.pygame.display.update(rects)

	def clear_updated(self):
		self.updated = []

	def set_running(self, running):
		self.running = running

