
import random
from lib.model.game_model_list import GameModelList
from lib.model.block import Block

# game grid for holding block game objects


class Grid(GameModelList):

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, game, block_class, block_size, grid_dimensions):
		super().__init__(game=game)
		self.Block = block_class
		self.block_width_px, self.block_height_px = block_size
		self.grid_width, self.grid_height = grid_dimensions
		self.grid = []
		for i in range(0, self.grid_height):
			row = []
			for k in range(0, self.grid_width):
				block = self.Block(
					game=game,
					surface=self.game.pygame.Surface(
						(self.block_width_px, self.block_height_px)
					),
					parent=self.game.screen,
					x_pos=k * self.block_width_px,
					y_pos=i * self.block_height_px,
					grid_index=(k, i)
				)
				row.append(block)
				self.add_game_model(block)
			self.grid.append(row)
		# self.occupied_blocks = {}

	def initialize(self):
		config = self.game.config
		for block in self.get_game_models():
			block.draw_color(
				color=config.GRID_BLOCK_COLOR,
				stroke_color=config.BLOCK_STROKE_COLOR,
				stroke_width=config.BLOCK_STROKE_PX_WIDTH
			)
			block.update()

	def get_block_at_grid_index(self, grid_index):
		x, y = grid_index
		if y >= 0 and y < len(self.grid):
			row = self.grid[y]
			if x >= 0 and x < len(row):
				return row[x]
		return None

	def get_adjacent_block_from_block(self, block, direction):
		x, y = block.get_grid_index()
		if direction == self.DIRECTION_UP:
			y = y - 1
		elif direction == self.DIRECTION_DOWN:
			y = y + 1
		elif direction == self.DIRECTION_LEFT:
			x = x - 1
		elif direction == self.DIRECTION_RIGHT:
			x = x + 1
		return self.get_block_at_grid_index((x, y))

	def get_random_block(self):
		row = random.choice(self.grid)
		block = random.choice(row)
		return block

	def get_random_line(self, line_length):
		row = row = random.choice(self.grid)
		line_start_index = random.choice(range(0, len(row) - line_length))
		line_end_index = line_start_index + line_length
		line_blocks = []
		for i in range(line_start_index, line_end_index):
			line_blocks.append(row[i])
		return line_blocks

	def get_parimeter(self):
		top_blocks = self.grid[0]
		bottom_blocks = self.grid[len(self.grid) - 1]
		left_blocks = []
		right_blocks = []
		for index, row in enumerate(self.grid):
			if index != 0 or index != len(row) - 1:
				left_blocks.append(row[0])
				right_blocks.append(row[len(row) - 1])
		return top_blocks + bottom_blocks + left_blocks + right_blocks

	def inspect(self):
		for block in self.get_game_models():
			block.inspect()

