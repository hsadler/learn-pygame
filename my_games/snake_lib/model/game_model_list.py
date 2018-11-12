
# game object list base class for all objects collections in game


class GameObjectList():

	def __init__(self, game_objects=[]):
		self.game_objects = game_objects


	def get_game_objects(self):
		return self.game_objects