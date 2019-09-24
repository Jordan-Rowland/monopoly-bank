"""Player class for each individual player."""

from time import sleep


class Player:
    """Player class, handles state regarding money, name, and properties."""
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.is_bankrupt = False

    def pay_bank(self, amount):
        """Handles basic transactions to the bank."""
        if self.is_bankrupt:
            return
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
            self.bankrupt()

    def pay_player(self, player, amount):
        """Handles paying other players for rent, etc."""
        if self.is_bankrupt:
            return
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
            self.bankrupt()

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

    def bankrupt(self):
        print('Would you like to declare bankruptcy? Yes or No')
        confirm = input('> ').lower()
        if confirm == 'yes':
            print('If you are sure, please type BANKRUPT. This action cannot be undone!')
            verify = input('> ')
            if verify == 'BANKRUPT':
                self.money = 0
                self.is_bankrupt = True
                print("Congratulations! You're bankrupt!")
                sleep(1)
