import random


def roll_dice() -> int:
    """
    Rolls a die. If the result is 6, the player will roll again and sum the results.

    Returns:
        int: The total sum of the dice rolls.
    """
    total: int = 0
    while True:
        turn: int = random.randint(1, 6)
        total += turn
        if turn != 6:
            break
    return total
