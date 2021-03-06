
import pygame

# game config model


class Config():

	GAME_NAME = 'snake'
	GAME_LOOP_RATE = 12

	SCREEN_PX_WIDTH = 1000
	SCREEN_PX_HEIGHT = 700

	BG_COLOR = pygame.Color('black')

	BLOCK_PX_WIDTH = 20
	BLOCK_PX_HEIGHT = 20
	BLOCK_STROKE_COLOR = pygame.Color('black')
	BLOCK_STROKE_PX_WIDTH = 1

	NONE_BLOCK_COLOR = pygame.Color('gray30')
	WALL_BLOCK_COLOR = pygame.Color('gray20')
	SNAKE_BLOCK_COLOR = pygame.Color('green')
	FOOD_BLOCK_COLOR = pygame.Color('yellow')

	GRID_WIDTH_BLOCKS = int(SCREEN_PX_WIDTH / BLOCK_PX_WIDTH)
	GRID_HEIGHT_BLOCKS = int(SCREEN_PX_HEIGHT / BLOCK_PX_HEIGHT)

	SNAKE_START_LENGTH = 20
	SNAKE_FOOD_COUNTDOWN = 10
	SNAKE_FED_DURATION = 5

	POINTS_TEXT_SIZE = 800
	POINTS_TEXT_COLOR = pygame.Color('gray80')
	POINTS_TEXT_ALPHA = 15

	RESTART_TEXT_SIZE = 120
	RESTART_TEXT_COLOR = pygame.Color('gray80')

	def __init__(self):
		self.pygame = pygame
		self.pygame.init()
		self.pygame.display.set_caption(self.GAME_NAME)

