
from lib.model.game_model_list import GameModelList

# game snake for holding block game objects
	# - manages block color draw
	# - manages block collidable property
	# - manages additions and removals of game blocks (simulate snake movement)


class Snake(GameModelList):

	def __init__(
		self,
		game,
		game_models=[],
		collidable=False,
		block_color=None
	):
		super().__init__(
			game=game,
			game_models=game_models,
			collidable=collidable,
			block_color=block_color
		)
		for block in self.game_models:
			block.set_color(self.block_color)
			block.draw()
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

	def get_head(self):
		return self.head['model']

	def get_tail(self):
		return self.tail['model']

	def append_head(self, head_model):
		new_head = {
			'model': head_model,
			'next': self.head,
			'prev': None
		}
		self.head['prev'] = new_head
		self.head = new_head
		self.add_game_model(game_model=head_model)
		head_model.set_color(self.block_color)
		head_model.draw()
		head_model.update()

	def pop_tail(self):
		new_tail = self.tail['prev']
		old_tail = self.tail
		old_tail['prev'] = None
		self.tail = new_tail
		self.remove_game_model(old_tail['model'])
		return old_tail['model']

	def move_snake(self, new_head, remove_tail=True):
		self.append_head(new_head)
		if remove_tail:
			return self.pop_tail()
		else:
			return None


