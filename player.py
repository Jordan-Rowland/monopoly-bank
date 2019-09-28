"""Player class for each individual player."""

from time import sleep


class Player:
    """Handles state regarding money, and name. If no money argument is provided, it will default
    to 1500, the amount players start with in a typical game. Money can be provided to restore a
    session if the program crashed. Provides methods for paying and collecting money, and
    bankrupting players."""

    def __init__(self, name: str, money: int = 1500):
        self.name = name
        self.money = money
        self.is_bankrupt = False

    def pay(self, amount: int, players: list = None):
        """Makes payments for things like properties or rent. Accepts an iterable of players for
        the players argument, and loops through(this allows 'pay all' community cards). If no
        players are provided, payment is made to 'the bank'. Aslo accepts an amount to be paid.
        Does not allow payment if the amount is more than the plaers current money, and prompts to
        bankrupt."""
        if self.is_bankrupt:
            return # Stops any payment if user is bankrupt
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
                print(f"{self.name} paid {player.name} ${amount}.")
        else:
            self.money -= amount
            print(f"{self.name} paid the bank ${amount}.")

    def collect(self, amount: int, players: list = None):
        """Receives money for things like rent, community cards, etc. Accepts an iterable as the
        players argument to allow community cards that collect from all players. If no players are
        provided, payment is from 'the bank'."""
        if players:
            for player in players:
                player.pay(amount, self)
        else:
            self.money += amount
            print(f"{self.name} received ${amount}.")

    def bankrupt(self):
        """Bankrupts a character with confirmation."""
        print("Would you like to declare bankruptcy? Yes or No")
        confirm = input("> ").lower()
        if confirm == "yes":
            print("If you are sure, please type BANKRUPT. This action cannot be undone!")
            verify = input("> ")
            if verify == "BANKRUPT":
                self.money = 0
                self.is_bankrupt = True
                print("Congratulations! You're bankrupt!")
                sleep(1)
