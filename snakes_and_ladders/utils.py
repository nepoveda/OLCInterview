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


LADDERS: [int, int] = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94,
}

SNAKES: [int, int] = {
    16: 6,
    46: 25,
    49: 11,
    62: 19,
    64: 60,
    74: 53,
    89: 68,
    92: 88,
    95: 75,
    99: 80,
}
