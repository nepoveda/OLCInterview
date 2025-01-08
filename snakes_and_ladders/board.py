class Board:
    def __init__(self, snakes: dict[int, int], ladders: dict[int, int]) -> None:
        """
        Initializes the Board with predefined positions for snakes and ladders.
        """
        self.snakes = snakes
        self.ladders = ladders

    def get_new_position(self, position: int) -> int:
        """
        Returns the new position of a player after encountering a snake or ladder.

        Args:
            position (int): The current position of the player.

        Returns:
            int: The new position of the player after moving up a ladder or down a snake.
        """
        if position in self.snakes:
            return self.snakes[position]
        elif position in self.ladders:
            return self.ladders[position]
        return position
