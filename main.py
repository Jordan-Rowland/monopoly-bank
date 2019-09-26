"""Main file to run the menu"""

from itertools import cycle

from player import Player
from game import Game
from menu import Menu


def main():
    """Asks how many players there are, and initializes the game. Runs the menu rotating through
    the players"""
    while True:
        try:
            num_players = int(input('How many players?\n> '))
            break
        except ValueError:
            print('Must be a valid number')
    player_list = list()
    for i in range(1, int(num_players) + 1):
        name = input(f'Player {i} name\n> ')
        player_list.append(Player(name))
#    P1 = Player('Rick')
#    P2 = Player('Jim')
#    P3 = Player('Dave')
#    PLAYERS = P1, P2, P3
    GAME = Game(player_list)
    MENU = Menu(GAME)
    for game_player in cycle(MENU.game.players):
        if not game_player.is_bankrupt:
            MENU.menu(game_player)


if __name__ == '__main__':
    main()
