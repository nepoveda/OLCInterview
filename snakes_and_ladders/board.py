class Board:
    def __init__(self):
        """
        Initializes the Board with predefined positions for snakes and ladders.
        """
        self.snakes: dict[int, int] = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78,
        }
        self.ladders: dict[int, int] = {
            1: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100,
        }

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
