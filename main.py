"""Main file to run the menu"""

from itertools import cycle

from player import Player
from game import Game
from menu import Menu


def main():
    num_players = input('How many players?\n> ')
    player_list = list()
    while True:
        try:
            for i in range(1, int(num_players) + 1):
                name = input(f'Player {i} name\n> ')
                player_list.append(Player(name))
            break
        except TypeError:
            print('Must be a valid number')
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
