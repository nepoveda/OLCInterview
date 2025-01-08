from game import Game

if __name__ == "__main__":
    num_players: int = int(input("Zadejte počet hráčů: "))
    game: "Game" = Game(num_players)
    game.play()
