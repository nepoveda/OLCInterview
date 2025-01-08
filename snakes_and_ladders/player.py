import typing

if typing.TYPE_CHECKING:
    from game import Game


class Player:
    def __init__(self, name: str, game: "Game"):
        self.name: str = name
        self.position: int = 1
        self.game: "Game" = game

    def move(self, steps: int) -> None:
        """
        Moves the player forward by a given number of steps and checks for collisions.

        Args:
            steps (int): The number of steps to move the player.
        """
        if self.position + steps <= 100:
            self.position += steps
            self.position = self.game.board.get_new_position(self.position)
            print(f"{self.name} se posunul na pole {self.position}")

            # Check if the new position is occupied by another player
            for player in self.game.players:
                if player != self and player.position == self.position:
                    player.move(-1)  # Move the other player back by one position
        else:
            print(f"{self.name} nemůže překročit pole 100")
