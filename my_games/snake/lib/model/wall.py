
from lib.model.game_model_list import GameModelList

# game wall for holding block game objects
	# - manages block color draw
	# - manages block collidable property


class Wall(GameModelList):

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
