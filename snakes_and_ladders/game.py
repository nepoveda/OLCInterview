import random
from board import Board
from player import Player

class Game:
    def __init__(self, num_players):
        self.board = Board()
        self.players = [Player(f"Hráč {i+1}") for i in range(num_players)]
        self.current_player_index = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        while True:
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name} je na poli {current_player.position}")
            roll = self.roll_dice()
            print(f"{current_player.name} hodil {roll}")
            current_player.move(roll)
            current_player.set_position(self.board.get_new_position(current_player.position))
            print(f"{current_player.name} se posunul na pole {current_player.position}")

            if current_player.position == 100:
                print(f"{current_player.name} vyhrál!")
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)