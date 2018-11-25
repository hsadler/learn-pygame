
# game model list base class for all object collections in game


class GameModelList():

	def __init__(
		self,
		game,
		game_models=[],
		collidable=False,
		block_color=None
	):
		self.game = game
		self.game_models = game_models
		self.collidable = collidable
		self.block_color = block_color

	def add_game_model(self, game_model):
		self.game_models.append(game_model)

	def get_game_models(self):
		return self.game_models

	def remove_game_model(self, game_model):
		self.game_models.remove(game_model)

	def get_block_color(self):
		return self.block_color

	def draw(self):
		for block in self.game_models:
			block.draw()

	def update(self):
		for model in self.game_models:
			model.update()
