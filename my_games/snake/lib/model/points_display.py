
from lib.model.game_model import GameModel

# points display object


class PointsDisplay(GameModel):

	def __init__(
		self,
		game,
		x_pos,
		y_pos
	):
		config = game.config
		surface = game.pygame.Surface(
			(config.SCREEN_PX_WIDTH, config.SCREEN_PX_HEIGHT)
		)
		surface.set_alpha(config.POINTS_TEXT_ALPHA)
		super().__init__(
			game=game,
			surface=surface,
			parent=game.screen,
			x_pos=x_pos,
			y_pos=y_pos,
			collidable=False
		)
		self.points = 0

	def draw(self):
		pygame = self.game.pygame
		config = self.game.config
		self.surface.fill(pygame.Color('black'))
		# write points to screen
		font = pygame.font.Font(None, config.POINTS_TEXT_SIZE)
		text = '{0}'.format(self.points)
		size = font.size(text)
		ren = font.render(text, 0, config.POINTS_TEXT_COLOR)
		self.surface.blit(
			ren,
			(
				config.SCREEN_PX_WIDTH/2 - size[0]/2,
				config.SCREEN_PX_HEIGHT/2 - size[1]/2
			)
		)
		self.update()

	def get_points(self):
		return self.points

	def increment_points(self):
		self.points += 1

	def inspect(self):
		print({
			'rect':	self.get_pos_rect(),
			'pos': [self.x, self.y],
			'collidable': self.collidable
		})
