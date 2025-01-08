from board import Board
from snakes_and_ladders.game import Game
from utils import SNAKES, LADDERS

if __name__ == "__main__":
    num_players: int = int(input("Zadejte počet hráčů: "))
    board: "Board" = Board(snakes=SNAKES, ladders=LADDERS)
    game: "Game" = Game(num_players, board)
    game.play()
