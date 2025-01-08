from board import Board
from player import Player
from snakes_and_ladders.utils import roll_dice


class Game:
    def __init__(self, num_players):
        """
        Initializes the Game with the specified number of players.

        Args:
            num_players (int): The number of players in the game.
        """
        self.board: Board = Board()
        self.players: list[Player] = [Player(f"Hráč {i+1}") for i in range(num_players)]
        self.current_player_index: int = 0

    def play(self) -> None:
        """
        Starts and controls the flow of the game until a player wins.
        """
        while True:
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name} je na poli {current_player.position}")
            roll = roll_dice()
            print(f"{current_player.name} hodil {roll}")
            # TODO check the possibility of move
            current_player.move(roll)
            current_player.set_position(
                self.board.get_new_position(current_player.position)
            )
            print(f"{current_player.name} se posunul na pole {current_player.position}")

            if current_player.position == 100:
                print(f"{current_player.name} vyhrál!")
                break

            self.current_player_index = (self.current_player_index + 1) % len(
                self.players
            )
