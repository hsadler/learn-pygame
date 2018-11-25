
from lib.model.game_model import GameModel

# block game object


class Block(GameModel):

	def __init__(
		self,
		game,
		surface,
		parent,
		x_pos,
		y_pos,
		grid_index,
		collidable=False,
		color=None,
		stroke_color=None,
		stroke_width=None
	):
		super().__init__(
			game=game,
			surface=surface,
			parent=parent,
			x_pos=x_pos,
			y_pos=y_pos,
			collidable=collidable
		)
		self.grid_index = grid_index
		self.color = color
		self.stroke_color = stroke_color
		self.stroke_width = stroke_width

	def draw(self):
		# block stroke fill
		stroke_rect = self.surface.get_rect()
		self.surface.fill(color=self.stroke_color, rect=stroke_rect)
		# block color fill
		block_color_rect = self.surface.get_rect().inflate(
			self.stroke_width * -1,
			self.stroke_width * -1
		)
		self.surface.fill(color=self.color, rect=block_color_rect)

	def get_grid_index(self):
		return self.grid_index

	def set_appearance(self, color, stroke_color, stroke_width):
		self.set_color(color)
		self.set_stroke_color(stroke_color)
		self.set_stroke_width(stroke_width)

	def set_color(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def set_stroke_color(self, stroke_color):
		self.stroke_color = stroke_color

	def get_stroke_color(self):
		return self.stroke_color

	def set_stroke_width(self, stroke_width):
		self.stroke_width = stroke_width

	def get_stroke_width(self):
		return self.stroke_width

	def get_string_formatted_grid_index(self):
		x, y = self.get_grid_index()
		return "x={0}__y={1}".format(x, y)

	def inspect(self):
		print({
			'rect':	self.get_pos_rect(),
			'pos': [self.x, self.y],
			'collidable': self.collidable
		})
