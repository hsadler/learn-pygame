
from lib.model.game_model_list import GameModelList
from lib.model.block import Block

# game grid for holding block game objects


class Grid(GameModelList):

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, game, block_class, block_size, grid_dimensions):
		super().__init__()
		self.game = game
		self.Block = block_class
		self.grid = []
		block_width_px, block_height_px = block_size
		grid_width, grid_height = grid_dimensions
		for i in range(0, grid_height):
			row = []
			for k in range(0, grid_width):
				block = self.Block(
					game=game,
					surface=self.game.pygame.Surface(
						(block_width_px, block_height_px)
					),
					parent=self.game.screen,
					x_pos=k * block_width_px,
					y_pos=i * block_height_px,
					grid_index=(k, i)
				)
				row.append(block)
				self.add_game_model(block)
			self.grid.append(row)

	def initialize(self):
		for block in self.get_game_models():
			block.update()

	def get_block_at_grid_index(self, grid_index):
		x, y = grid_index
		if y >= 0 and y < len(self.grid):
			row = self.grid[y]
			if x >= 0 and x < len(row):
				return row[x]
		return None

	def get_adjacent_block_from_selected(self, direction):
		x, y = self.selected_block.get_grid_index()
		if direction == self.DIRECTION_UP:
			y = y - 1
		elif direction == self.DIRECTION_DOWN:
			y = y + 1
		elif direction == self.DIRECTION_LEFT:
			x = x - 1
		elif direction == self.DIRECTION_RIGHT:
			x = x + 1
		return self.get_block_at_grid_index((x, y))

	def inspect(self):
		for block in self.get_game_models():
			block.inspect()

