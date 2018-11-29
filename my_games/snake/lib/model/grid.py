
import random
from lib.model.game_model_list import GameModelList
from lib.model.block import Block

# game grid for holding block game objects
	# - manages block collision detection
	# - manages block updates to display


class Grid(GameModelList):

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(
		self,
		game,
		block_class,
		block_size,
		block_color,
		grid_dimensions
	):
		super().__init__(game=game)
		self.Block = block_class
		self.block_width_px, self.block_height_px = block_size
		self.block_color = block_color
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
		self.occupied_blocks = {}

	def initialize(self):
		config = self.game.config
		for block in self.get_game_models():
			block.set_appearance(
				color=config.NONE_BLOCK_COLOR,
				stroke_color=config.BLOCK_STROKE_COLOR,
				stroke_width=config.BLOCK_STROKE_PX_WIDTH
			)
			block.draw()

	def update_all_blocks(self):
		config = self.game.config
		for block in self.get_game_models():
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

	def get_rand_avail_block(self):
		selected_block = None
		while selected_block is None:
			rand_block = self.get_random_block()
			rand_block_key = rand_block.get_string_formatted_grid_index()
			if rand_block_key not in self.occupied_blocks:
				selected_block = rand_block
		return selected_block

	def get_random_line(self, line_length):
		row = random.choice(self.grid)
		line_start_index = random.choice(range(0, len(row) - line_length))
		line_end_index = line_start_index + line_length
		return row[line_start_index:line_end_index]

	def get_center_horiz_line(self, line_length):
		row = self.grid[int(len(self.grid) / 2)]
		line_start_index = int(len(row) / 2) - int(line_length / 2)
		line_end_index = line_start_index + line_length
		return row[line_start_index:line_end_index]

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

	def update_occupied_blocks(self, add=[], remove=[]):
		for block in add:
			block_key = block.get_string_formatted_grid_index()
			self.occupied_blocks[block_key] = block
		for block in remove:
			block_key = block.get_string_formatted_grid_index()
			if block_key in self.occupied_blocks:
				del self.occupied_blocks[block_key]

	def check_collision(self, add=[], remove=[]):
		occupied_blocks_copy = dict(self.occupied_blocks)
		for block in remove:
			block_key = block.get_string_formatted_grid_index()
			if block_key in occupied_blocks_copy:
				del occupied_blocks_copy[block_key]
		for block in add:
			block_key = block.get_string_formatted_grid_index()
			if (
				block_key in occupied_blocks_copy and
				block.get_collidable() and
				occupied_blocks_copy[block_key].get_collidable()
			):
				return True
		return False

	def inspect(self):
		for block in self.get_game_models():
			block.inspect()

