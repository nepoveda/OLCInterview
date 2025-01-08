class Player:
    def __init__(self, name: str):
        """
        Initializes a Player with a given name and starting position.

        Args:
            name (str): The name of the player.
        """
        self.name: str = name
        self.position: int = 0

    def move(self, steps: int) -> None:
        """
        Moves the player forward by a given number of steps.

        Args:
            steps (int): The number of steps to move the player.
        """
        self.position += steps

    def set_position(self, position: int) -> None:
        """
        Sets the player's position to a specific value.

        Args:
            position (int): The new position of the player.
        """
        self.position = position
