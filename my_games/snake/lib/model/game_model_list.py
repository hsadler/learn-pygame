
# game model list base class for all object collections in game


class GameModelList():

	def __init__(self, game, game_models=[]):
		self.game = game
		self.game_models = game_models

	def add_game_model(self, game_model):
		self.game_models.append(game_model)

	def get_game_models(self):
		return self.game_models