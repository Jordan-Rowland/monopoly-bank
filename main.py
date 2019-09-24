"""Banking system for games of Monopoly board game."""

from itertools import cycle
from time import sleep

from player import Player
from game import Game

class Menu:
    def __init__(self, game):
        self.game = game
    
    def menu(self, player):
        """Displays the top-level menu beginning each players turn."""
        while True:
            print()
            if player.is_bankrupt:
                return
            sleep(1)
            print(f'Community pot - ${self.game.community_pot}')
            for iplayer in self.game.players:
                print(f'{iplayer.name} - ${iplayer.money}', end='\t')
            print(f'\n{"=" * 75}')
            print(f'Current turn: {player.name} - ${player.money}\n')
            print(
                "Choose an action:\n"
                "(R) Roll\n"
                "(P) Pay...\n"
                "(C) Collect money\n"
                "(G) Pass Go(collect $200)\n"
                "(E) End turn\n"
            )
            action = input('> ').lower()
            if action == 'r':
                self.game.roll()
            elif action == 'p':
                self.pay_menu(player)
                print()
            elif action == 'c':
                self.collect_menu(player)
                print()
            elif action == 'g':
                player.receive_from_bank(200)
            elif action == 'e':
                break

    def pay_menu(self, player):
        """Access this to determine who the current player will pay."""
        print(f'\n{"=" * 25}')
        amount = -1
        selected_player = None
        print('Choose who to pay:\n')
        print(
            "(P) Pay Player\n"
            "(B) Pay Bank\n"
            "(C) Pay Community Pot\n"
            "(E) Pay Everyone\n"
        )
        pay_action = input('> ').lower()
        if pay_action == 'p':
            selected_player = self.select_user_menu(player)
        while amount < 0:
            try:
                amount = int(input('How much?\n> '))
            except ValueError:
                print('Must select a numerical value')
        if selected_player:
            player.pay_player(selected_player, amount)
        elif pay_action == 'b':
            player.pay_bank(amount)
        elif pay_action == 'c':
            self.game.pay_community_pot(player, amount)
        elif pay_action == 'e':
            player.pay_all_players(self.game.players, amount)

    def collect_menu(self, player):
        """Access this to determine from who the current player will collect money
        from."""
        print(f'\n{"=" * 25}')
        amount = -1
        print('Collect from:\n')
        print(
            "(C) Community Pot\n"
            "(B) Bank\n"
            "(E) Everyone\n"
        )
        collect_action = input('> ').lower()
        if collect_action == 'c':
            amount = self.game.community_pot
            self.game.get_community_pot(player)
        while amount < 0:
            try:
                amount = int(input('How much?\n> '))
            except ValueError:
                print('Must select a numerical value')
        if collect_action == 'b':
            player.receive_from_bank(amount)
        elif collect_action == 'e':
            player.receive_from_players(self.game.players, amount)

    def select_user_menu(self, player):
        """Returns the Player object of the player whose name is typed in."""
        selected_player = None
        while not selected_player:
            try:
                print(f'\n{"=" * 25}')
                print('Select a player:\n')
                for other_player in self.game.players:
                    if other_player != player:
                        print(other_player.name)
                selected_name = input('> ').lower()
                selected_player = [player for player in self.game.players
                                   if player.name.lower() == selected_name][0]
            except IndexError:
                print()
                print('Could not find user.')
                sleep(1)
        return selected_player


if __name__ == '__main__':
    P1 = Player('Rick')
    P2 = Player('Jim')
    P3 = Player('Dave')
    GAME = Game(P1, P2, P3)
    MENU = Menu(GAME)
    for game_player in cycle(MENU.game.players):
        if not game_player.is_bankrupt:
            MENU.menu(game_player)
