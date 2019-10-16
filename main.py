"""Main file to run the menu"""

from itertools import cycle

from player import Player
from game import Game
from menu import Menu


def main(game: Game = None):
    """Accepts an argument which is an initialized Game instance. This is used to restore a game to
    it's previous state if the program crashed. If no argument is provided, it will ask how many
    players there are, and initialize all Players and the game instance, and then run the menu."""
    if not game:
        while True:
            try:
                num_players = int(input("How many players?\n> "))
                break
            except ValueError:
                print("Must be a valid number")
        player_list = list()
        for i in range(1, num_players + 1):
            name = input(f"Player {i} name\n> ")
            player_list.append(Player(name))
        GAME = Game(player_list)
    else:
        GAME = game
    MENU = Menu(GAME)
    for game_player in cycle(MENU.game.players):
        if not game_player.is_bankrupt:
            MENU.menu(game_player)


if __name__ == "__main__":
    main()
