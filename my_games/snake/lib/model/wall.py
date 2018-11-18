
from lib.model.game_model_list import GameModelList

# game wall for holding block game objects


class Wall(GameModelList):

	def update(self):
		config = self.game.config
		for block in self.game_models:
			block.draw_color(
				color=config.WALL_BLOCK_COLOR,
				stroke_color=config.BLOCK_STROKE_COLOR,
				stroke_width=config.BLOCK_STROKE_PX_WIDTH
			)
			block.update()