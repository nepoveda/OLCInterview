from snakes_and_ladders.board import Board
from snakes_and_ladders.game import Game
from snakes_and_ladders.utils import SNAKES, LADDERS

num_players: int = int(input("Zadejte počet hráčů: "))
board: "Board" = Board(snakes=SNAKES, ladders=LADDERS)
game: "Game" = Game(num_players, board)
game.play()
