
from snake_lib.game_object import GameObject

# block game object


class Block(GameObject):

	def __init__(self, surface, parent, x_pos, y_pos, grid_index):
		super().__init__(
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
			BLOCK_STROKE_PX_WIDTH * -1,
			BLOCK_STROKE_PX_WIDTH * -1
		)
		self.surface.fill(color=color, rect=block_color_rect)

	def update(self, is_selected=False):
		color = BLOCK_SELECTED_COLOR if is_selected else BLOCK_COLOR
		self.draw_color(
			color=color,
			stroke_color=BLOCK_STROKE_COLOR,
			stroke_width=BLOCK_STROKE_PX_WIDTH
		)
		super().update()

	def get_is_selected(self):
		return self.is_selected

	def get_grid_index(self):
		return self.grid_index

	def inspect(self):
		print({
			'rect':	self.get_pos_rect(),
			'pos': [self.x, self.y]
		})
