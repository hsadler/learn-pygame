
from lib.model.config import Config
from lib.model.game import Game
from lib.business.game import GameBL


def main():

	# create config
	config = Config()
	# create game manager
	game = Game(config=config)

	def run_game():
		# create and init new game business logic
		game_bl = GameBL(game=game)
		game_bl.init_new_game()
		# game loop
		while game.get_running():
			game_bl.run_game_loop()

	while game.get_restart():
		run_game()


if __name__=="__main__":
	main()

