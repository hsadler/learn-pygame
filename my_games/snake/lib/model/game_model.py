
# game model base class for all objects in game


class GameModel():

	def __init__(self, game, surface, parent, x_pos, y_pos, collidable=False):
		self.game = game
		self.surface = surface
		self.parent = parent
		self.x = x_pos
		self.y = y_pos
		self.collidable = collidable

	def move(self, x_amount, y_amount):
		self.x += x_amount
		self.y += y_amount

	def update(self):
		self.parent.blit(self.surface, (self.x, self.y))

	def get_pos_rect(self):
		return self.surface.get_rect(
			center=(
				self.x + self.surface.get_width() / 2,
				self.y + self.surface.get_height() / 2
			)
		)

	def set_collidable(self, val):
		self.collidable = val

	def get_collidable(self):
		return self.collidable

