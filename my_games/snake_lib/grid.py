
from snake_lib.game_object_list import GameObjectList
from snake_lib.block import Block

# game grid for holding block game objects


class Grid(GameObjectList):

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, game):
		self.game = game
		self.blocks_width = self.game.config.GRID_WIDTH_BLOCKS
		self.blocks_height = self.game.config.GRID_HEIGHT_BLOCKS
		self.block_width_px = self.game.config.BLOCK_PX_WIDTH
		self.block_height_px = self.game.config.BLOCK_PX_HEIGHT
		self.grid = []
		# single dimension array for easy iteration
		self.block_list = []
		for i in range(0, self.blocks_height):
			row = []
			for k in range(0, self.blocks_width):
				block = Block(
					surface=self.game.pygame.Surface(
						(self.block_width_px, self.block_height_px)
					),
					parent=self.game.screen,
					x_pos=k * self.block_width_px,
					y_pos=i * self.block_height_px,
					grid_index=(k, i)
				)
				row.append(block)
				self.block_list.append(block)
			self.grid.append(row)

	def get_block_at_grid_index(self, grid_index):
		x, y = grid_index
		if y >= 0 and y < len(self.grid):
			row = self.grid[y]
			if x >= 0 and x < len(row):
				return row[x]
		return None

	def get_direction_from_user_input(self):
		pressed = self.pygame.key.get_pressed()
		if pressed[self.pygame.K_w]:
			return self.DIRECTION_UP
		elif pressed[self.pygame.K_d]:
			return self.DIRECTION_RIGHT
		elif pressed[self.pygame.K_a]:
			return self.DIRECTION_LEFT
		elif pressed[self.pygame.K_s]:
			return self.DIRECTION_DOWN
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
		for block in self.block_list:
			block.inspect()

