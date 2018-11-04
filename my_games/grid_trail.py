

import pygame
import sys


SCREEN_PX_WIDTH = 1000
SCREEN_PX_HEIGHT = 700

BG_COLOR = pygame.Color('black')

BLOCK_PX_WIDTH = 10
BLOCK_PX_HEIGHT = 10
BLOCK_COLOR = pygame.Color('gray30')
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
		self.surface.fill(color=BLOCK_COLOR, rect=block_color_rect)
	def update(self):
		self.draw_color(
			color=BLOCK_COLOR,
			stroke_color=BLOCK_STROKE_COLOR,
			stroke_width=BLOCK_STROKE_PX_WIDTH
		)
		self.parent.blit(self.surface, (self.x, self.y))
		# super().update()
	def inspect(self):
		print({
			'rect':	self.get_pos_rect(),
			'pos': [self.x, self.y]
		})

class Grid():
	def __init__(self, screen, width, height, block_size):
		self.width = width
		self.height = height
		self.block_width_px = block_size[0]
		self.block_height_px = block_size[1]
		self.grid = []
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
				row.append(block)
			self.grid.append(row)
	def update(self):
		for row in self.grid:
			for block in row:
				block.update()
	def inspect(self):
		for row in self.grid:
			for block in row:
				block.inspect()


def main():

	# initialize the pygame module
	pygame.init()
	# set the caption at top of game window
	pygame.display.set_caption("game template")
	# create a surface on screen
	screen = pygame.display.set_mode((SCREEN_PX_WIDTH, SCREEN_PX_HEIGHT))

	# background
	background = GameObject(
		surface=pygame.Surface(screen.get_size()),
		parent=screen,
		x_pos=0,
		y_pos=0
	)
	background.surface.fill(color=BG_COLOR)
	background.update()

	# grid
	grid = Grid(
		screen=screen,
		width=GRID_WIDTH_BLOCKS,
		height=GRID_HEIGHT_BLOCKS,
		block_size=(BLOCK_PX_WIDTH, BLOCK_PX_HEIGHT)
	)
	# update all the blocks in the grid
	grid.update()

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

		# update game objects
		background.update()
		grid.update()

		# update display
		pygame.display.update()


if __name__=="__main__":
	main()
