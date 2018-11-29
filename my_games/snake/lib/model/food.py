
from lib.model.game_model_list import GameModelList

# game food for holding block game objects
	# - manages block color draw
	# - manages block collidable property


class Food(GameModelList):

	def __init__(
		self,
		game,
		game_model,
		collidable=False,
		block_color=None
	):
		super().__init__(
			game=game,
			game_models=[game_model],
			collidable=collidable,
			block_color=block_color
		)
		for block in self.game_models:
			block.set_color(self.block_color)
			block.draw()

	def get_block(self):
		return self.get_game_models()[0]
