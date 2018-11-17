
from lib.model.game_model import GameModel

# block game object


class Block(GameModel):

	def __init__(self, game, surface, parent, x_pos, y_pos, grid_index):
		super().__init__(
			game=game,
			surface=surface,
			parent=parent,
			x_pos=x_pos,
			y_pos=y_pos
		)
		self.grid_index = grid_index

	def draw_color(self, color, stroke_color, stroke_width):
		# block stroke fill
		stroke_rect = self.surface.get_rect()
		self.surface.fill(color=stroke_color, rect=stroke_rect)
		# block color fill
		block_color_rect = self.surface.get_rect().inflate(
			stroke_width * -1,
			stroke_width * -1
		)
		self.surface.fill(color=color, rect=block_color_rect)

	def get_grid_index(self):
		return self.grid_index

	def inspect(self):
		print({
			'rect':	self.get_pos_rect(),
			'pos': [self.x, self.y]
		})
