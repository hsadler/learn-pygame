

import pygame
import random
import sys


GAME_LOOP_RATE = 30

SCREEN_PX_WIDTH = 1000
SCREEN_PX_HEIGHT = 700

BG_COLOR = pygame.Color('black')

BLOCK_PX_WIDTH = 10
BLOCK_PX_HEIGHT = 10
BLOCK_COLOR = pygame.Color('gray30')
BLOCK_SELECTED_COLOR = pygame.Color('green')
BLOCK_STROKE_COLOR = pygame.Color('black')
BLOCK_STROKE_PX_WIDTH = 1

GRID_WIDTH_BLOCKS = int(SCREEN_PX_WIDTH / BLOCK_PX_WIDTH)
GRID_HEIGHT_BLOCKS = int(SCREEN_PX_HEIGHT / BLOCK_PX_HEIGHT)


class GameObject():
	def __init__(self, surface, parent, x_pos, y_pos):
		self.surface = surface
		self.parent = parent
		self.x = x_pos
		self.y = y_pos
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

class Grid():

	DIRECTION_UP = 'up'
	DIRECTION_DOWN = 'down'
	DIRECTION_LEFT = 'left'
	DIRECTION_RIGHT = 'right'

	def __init__(self, screen, width, height, block_size):
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
					surface=pygame.Surface(block_size),
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
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_w]:
			return self.DIRECTION_UP
		elif pressed[pygame.K_d]:
			return self.DIRECTION_RIGHT
		elif pressed[pygame.K_a]:
			return self.DIRECTION_LEFT
		elif pressed[pygame.K_s]:
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


def main():

	# initialize the pygame module
	pygame.init()
	# set the caption at top of game window
	pygame.display.set_caption("game template")
	# create a surface on screen
	screen = pygame.display.set_mode((SCREEN_PX_WIDTH, SCREEN_PX_HEIGHT))
	# get instance of the game clock
	game_clock = pygame.time.Clock()

	# grid
	grid = Grid(
		screen=screen,
		width=GRID_WIDTH_BLOCKS,
		height=GRID_HEIGHT_BLOCKS,
		block_size=(BLOCK_PX_WIDTH, BLOCK_PX_HEIGHT)
	)
	# set random block as selected
	grid.select_random_block()
	# update all the blocks in the grid as initialization step
	grid.update()

	# initialize with entire display update
	pygame.display.update()

	# game loop
	running = True
	while running:

		# exit event conditions
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.unicode == 'q':
					running = False

		# block selection based on user input
		direction = grid.get_direction_from_user_input()
		if direction is not None:
			new_selected_block = grid.get_adjacent_block_from_selected(
				direction=direction
			)
			if new_selected_block:
				grid.select_block(new_selected_block)

		# update game objects
		grid.update_selected()

		# update display only selected block
		pygame.display.update(grid.get_updated_rect())

		# lock game loop rate
		game_clock.tick(GAME_LOOP_RATE)


if __name__=="__main__":
	main()

