
import pygame
import sys


# game configuration
BG_COLOR = pygame.Color('black')

WALL_GIRTH = 50
WALL_COLOR = pygame.Color('green')

SQ_WIDTH = 20
SQ_HEIGHT = 20
SQ_SPEED = 4
SQ_COLOR = pygame.Color('grey')


# define a game object with parent, color, and position
class GameObject():
	def __init__(self, obj, parent, color, x_pos, y_pos):
		self.obj = obj
		self.obj.fill(color)
		self.parent = parent
		self.x = x_pos
		self.y = y_pos
	def move(self, x_amount, y_amount):
		self.x += x_amount
		self.y += y_amount
	def update(self):
		self.parent.blit(self.obj, (self.x, self.y))
	def get_pos_rect(self, x_offset=0, y_offset=0):
		return self.obj.get_rect(
			center=(
				self.x + self.obj.get_width() / 2 + x_offset,
				self.y + self.obj.get_height() / 2 + y_offset
			)
		)

# define walls collection
class Walls():
	def __init__(self):
		self.objs = []
	def add(self, parent, size, position):
		wall = GameObject(
			obj=pygame.Surface((size[0], size[1])),
			parent=parent,
			color=WALL_COLOR,
			x_pos=position[0],
			y_pos=position[1]
		)
		self.objs.append(wall)
	def get(self):
		return self.objs
	def update(self):
		for wall in self.objs:
			wall.update()
	def get_pos_rects(self):
		pos_rects = []
		for wall in self.objs:
			pos_rects.append(wall.get_pos_rect())
		return pos_rects

# define square (player controlled object)
class Square(GameObject):
	def __init__(self, obj, parent, color, x_pos, y_pos, speed):
		super().__init__(
			obj=obj,
			parent=parent,
			color=color,
			x_pos=x_pos,
			y_pos=y_pos
		)
		self.speed = speed
	def controller_move(self):
		new_offset = self.get_position_offset_from_controller_input()
		self.move(x_amount=new_offset[0], y_amount=new_offset[1])
	def get_position_offset_from_controller_input(self):
		pressed = pygame.key.get_pressed()
		offset = (0, 0)
		if pressed[pygame.K_w]:
			offset = (0, -1)
		elif pressed[pygame.K_d]:
			offset = (1, 0)
		elif pressed[pygame.K_a]:
			offset = (-1, 0)
		elif pressed[pygame.K_s]:
			offset = (0, 1)
		offset = (offset[0] * self.speed, offset[1] * self.speed)
		return offset
	def check_potential_collisions(self, game_objects=[]):
		new_square_position = self.get_position_offset_from_controller_input()
		new_square_rect = self.get_pos_rect(
			x_offset=new_square_position[0],
			y_offset=new_square_position[1]
		)
		game_object_rects = []
		for obj in game_objects:
			game_object_rects.append(obj.get_pos_rect())
		return pygame.Rect.collidelist(new_square_rect, game_object_rects) > -1


def main():

	# initialize the pygame module
	pygame.init()

	# set the caption at top of game window
	pygame.display.set_caption("move square")

	# create screen surface
	screen = pygame.display.set_mode((1000, 700))

	# create background

	background = GameObject(
		obj=pygame.Surface(screen.get_size()),
		parent=screen,
		color=BG_COLOR,
		x_pos=0,
		y_pos=0
	)
	background.update()

	# create static walls
	walls = Walls()
	# left wall
	walls.add(
		parent=screen,
		size=(WALL_GIRTH, screen.get_height()),
		position=(0, 0)
	)
	# right wall
	walls.add(
		parent=screen,
		size=(WALL_GIRTH, screen.get_height()),
		position=(screen.get_width() - WALL_GIRTH, 0)
	)
	# top wall
	walls.add(
		parent=screen,
		size=(screen.get_width() - WALL_GIRTH * 2, WALL_GIRTH),
		position=(WALL_GIRTH, 0)
	)
	# bottom wall
	walls.add(
		parent=screen,
		size=(screen.get_width() - WALL_GIRTH * 2, WALL_GIRTH),
		position=(WALL_GIRTH, screen.get_height() - WALL_GIRTH)
	)
	walls.update()

	# player controlled square
	square = Square(
		obj=pygame.Surface((SQ_WIDTH, SQ_HEIGHT)),
		parent=screen,
		color=SQ_COLOR,
		x_pos=screen.get_width() / 2 - SQ_WIDTH / 2,
		y_pos=screen.get_height() / 2 - SQ_HEIGHT / 2,
		speed=SQ_SPEED
	)
	square.update()

	# game loop
	running = True
	while running:

		# event handling, gets all events from the eventqueue
		for event in pygame.event.get():
			# exit event conditions
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE or event.unicode == 'q':
					running = False

		# update background and wall
		background.update()
		walls.update()

		# check if square has collided with any wall
		if not square.check_potential_collisions(game_objects=walls.get()):
			square.controller_move()
		square.update()

		pygame.display.update()


if __name__=="__main__":
	main()
