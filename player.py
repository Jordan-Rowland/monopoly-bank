"""Player class for each individual player."""

from time import sleep


class Player:
    """Player class, handles state regarding money, name, and properties."""
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.is_bankrupt = False

    def pay(self, amount, players=None):
        """Handles money playment. If no players are provided, payment is made to 'the bank'."""
        if self.is_bankrupt:
            return
        if self.money < amount:
            print()
            print(
                f"{self.name} does not have enough money for this transaction.\n"
                "Please sell some assets, or declare bankruptcy"
            )
            self.bankrupt()
            return
        if players:
            if not isinstance(players, list):
                players = [players]
            for player in players:
                self.money -= amount
                player.money += amount
                print(f'{self.name} paid {player.name} ${amount}.')
        else:
            self.money -= amount
            print(f'{self.name} paid the bank ${amount}.')

    def collect(self, amount, players=None):
        """Handles receiving money. If no players are provided, payment is from 'the bank'."""
        if players:
            for player in players:
                player.pay(amount, self)
        else:
            self.money += amount
            print(f'{self.name} received ${amount}.')

    def bankrupt(self):
        """Bankrupts a character with confirmation."""
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
