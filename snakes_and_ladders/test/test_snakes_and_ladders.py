import unittest
from ..board import Board
from ..player import Player
from ..game import Game


class TestBoard(unittest.TestCase):
    def test_initializes_with_snakes_and_ladders(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        self.assertEqual(board.snakes[16], 6)
        self.assertEqual(board.ladders[1], 38)

    def test_returns_new_position_for_snake(self):
        snakes = {16: 6}
        ladders = {}
        board = Board(snakes, ladders)
        self.assertEqual(board.get_new_position(16), 6)

    def test_returns_new_position_for_ladder(self):
        snakes = {}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        self.assertEqual(board.get_new_position(1), 38)

    def test_returns_same_position_if_no_snake_or_ladder(self):
        snakes = {}
        ladders = {}
        board = Board(snakes, ladders)
        self.assertEqual(board.get_new_position(2), 2)


class TestPlayer(unittest.TestCase):
    def test_initializes_with_name_and_position(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(1, board)
        player = Player("Player 1", game)
        self.assertEqual(player.name, "Player 1")
        self.assertEqual(player.position, 1)

    def test_moves_forward_by_steps(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(1, board)
        player = Player("Player 1", game)
        player.move(3)
        self.assertEqual(player.position, 4)

    def test_moves_back_if_lands_on_other_player(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(2, board)
        player1 = game.players[0]
        player2 = game.players[1]
        player1.move(3)
        player2.move(3)
        self.assertEqual(player2.position, 4)
        self.assertEqual(player1.position, 3)

    def test_does_not_move_beyond_100(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(1, board)
        player = Player("Player 1", game)
        player.position = 99
        player.move(2)
        self.assertEqual(player.position, 99)


class TestGame(unittest.TestCase):
    def test_initializes_with_correct_number_of_players(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(2, board)
        self.assertEqual(len(game.players), 2)

    def test_player_wins_when_reaches_100(self):
        snakes = {16: 6}
        ladders = {1: 38}
        board = Board(snakes, ladders)
        game = Game(1, board)
        player = game.players[0]
        player.position = 99
        player.move(1)
        self.assertEqual(player.position, 100)


if __name__ == "__main__":
    unittest.main()
