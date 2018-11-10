
# game grid for holding block game objects


class Grid(GameObjectList):

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, pygame, screen, width, height, block_size):
		self.pygame = pygame
		self.width = width
		self.height = height
		self.block_width_px = block_size[0]
		self.block_height_px = block_size[1]
		self.grid = []
		# single dimension array for easy iteration
		self.block_list = []
		self.updated_blocks = []
		self.selected_block = None
		for i in range(0, self.height):
			row = []
			for k in range(0, width):
				block = Block(
					surface=self.pygame.Surface(block_size),
					parent=screen,
					x_pos=k * self.block_width_px,
					y_pos=i * self.block_height_px,
					grid_index=(k, i)
				)
				self.block_list.append(block)
				row.append(block)
			self.grid.append(row)

	def update(self):
		for block in self.block_list:
			is_selected = self.selected_block == block
			block.update(is_selected=is_selected)

	def update_selected(self):
		self.selected_block.update(is_selected=True)

	def get_updated_rect(self):
		return self.selected_block.get_pos_rect()

	def select_block(self, block):
		self.selected_block = block

	def select_random_block(self):
		self.selected_block = random.choice(self.block_list)

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

