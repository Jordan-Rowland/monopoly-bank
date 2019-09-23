"""Banking system for games of Monopoly board game."""


from itertools import cycle
from time import sleep


class Game:
    """Retains main game state and displays UI menu."""
    def __init__(self, players):
        self.players = players
        self.community_pot = 0

    def pay_community_pot(self, player, amount):
        """Pays into community pot for payments not directly to the bank."""
        player.money -= amount
        self.community_pot += amount
        print(f'{player.name} put ${amount} into the community pot.')

    def get_community_pot(self, player):
        """Gives entire community pot to a player. Use this when a user lands on
        the 'free parking' space."""
        player.money += self.community_pot
        print(f'{player.name} earned ${self.community_pot} from the community pot.')
        self.community_pot = 0

    def menu(self, player):
        """Displays the top-level menu beginning each players turn."""
        print()
        while True:
            print(f'Community pot - ${self.community_pot}')
            for iplayer in self.players:
                print(f'{iplayer.name} - ${iplayer.money}', end='\t')
            print(f'\n{"=" * 75}')
            print(f'Current turn: {player.name} - ${player.money}\n')
            print(
                "Choose an action:\n"
                "(P) Pay...\n"
                "(C) Collect money\n"
                "(G) Pass Go(collect $200)\n"
                "(E) End turn\n"
            )
            action = input('> ').lower()
            if action == 'p':
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
        amount = None
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
        while not amount:
            try:
                amount = int(input('How much?\n> '))
            except ValueError:
                print('Must select a numerical value')
        if selected_player:
            player.pay_player(selected_player, amount)
        elif pay_action == 'b':
            player.pay_bank(amount)
        elif pay_action == 'c':
            self.pay_community_pot(player, amount)
        elif pay_action == 'e':
            player.pay_all_players(self.players, amount)

    def collect_menu(self, player):
        """Access this to determine from who the current player will collect money
        from."""
        print(f'\n{"=" * 25}')
        amount = None
        print('Collect from:\n')
        print(
            "(B) Bank\n"
            "(C) Community Pot\n"
            "(E) Everyone\n"
        )
        collect_action = input('> ').lower()
        while not amount:
            try:
                amount = int(input('How much?\n> '))
            except ValueError:
                print('Must select a numerical value')
        if collect_action == 'b':
            player.receive_from_bank(amount)
        elif collect_action == 'c':
            GAME.get_community_pot(player)
        elif collect_action == 'e':
            player.receive_from_players(self.players, amount)

    def select_user_menu(self, player):
        """Returns the Player object of the player whose name is typed in."""
        selected_player = None
        while not selected_player:
            try:
                print(f'\n{"=" * 25}')
                print('Select a player:\n')
                for other_player in self.players:
                    if other_player != player:
                        print(other_player.name)
                selected_name = input('> ').lower()
                selected_player = [player for player in GAME.players
                                   if player.name.lower() == selected_name][0]
            except IndexError:
                print()
                print('Could not find user.')
        return selected_player


class Player:
    """Player class, handles state regarding money, name, and properties."""
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.is_bankrupt = False

    def pay_bank(self, amount):
        """Handles basic transactions to the bank."""
        if self.money > amount:
            self.money -= amount
            print(f'{self.name} paid the bank ${amount}.')
        else:
            print()
            print(
                f"{self.name} does not have enough money for this transaction.\n"
                "Please sell some assets, or declare bankruptcy"
            )
            sleep(1)

    def pay_player(self, player, amount):
        """Handles paying other players for rent, etc."""
        if self.money > amount:
            self.money -= amount
            player.money += amount
            print(f'{self.name} paid {player.name} ${amount}.')
        else:
            print()
            print(
                f"{self.name} does not have enough money for this transaction.\n"
                "Please sell some assets, or declare bankruptcy"
            )
            sleep(1)

    def receive_from_bank(self, amount):
        """Handles receiving money from community chest cards, etc."""
        self.money += amount
        print(f'{self.name} received ${amount}.')

    def receive_from_players(self, players, amount):
        """Handles payment from all other players from community chest cards, etc."""
        for player in players:
            player.pay_player(self, amount)

    def pay_all_players(self, players, amount):
        """Handles paying all players from chance cards, etc."""
        for player in players:
            self.pay_player(player, amount)


if __name__ == '__main__':
    P1 = Player('Rick')
    P2 = Player('Jim')
    P3 = Player('Dave')
    GAME = Game([P1, P2, P3])
    for game_player in cycle(GAME.players):
        if not game_player.is_bankrupt:
            GAME.menu(game_player)
