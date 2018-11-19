
from lib.model.game_model_list import GameModelList

# game snake for holding block game objects


class Snake(GameModelList):

	# DIRECTION_UP = 'up'
	# DIRECTION_DOWN = 'down'
	# DIRECTION_LEFT = 'left'
	# DIRECTION_RIGHT = 'right'

	def __init__(self, game, game_models=[]):
		if len(game_models) < 2:
			return None
		super().__init__(game=game, game_models=game_models)
		self.head = {
			'model': game_models[0],
			'next': None,
			'prev': None
		}
		last = self.head
		for index, game_model in enumerate(game_models):
			if index > 0:
				new = {
					'model': game_model,
					'next': None,
					'prev': last
				}
				last['next'] = new
				last = last['next']
			if index == len(game_models) - 1:
				self.tail = new

	def update(self):
		config = self.game.config
		for block in self.game_models:
			block.draw_color(
				color=config.SNAKE_BLOCK_COLOR,
				stroke_color=config.BLOCK_STROKE_COLOR,
				stroke_width=config.BLOCK_STROKE_PX_WIDTH
			)
			block.update()

	def get_head(self):
		return self.head

	def get_tail(self):
		return self.tail

	def move_snake(self, new_head, remove_tail=True):
		pass


