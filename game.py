"""Game instance."""

from random import choice

from player import Player


class Game:
    """Maintains game state. Accepts initialized Player objects for players of the current game.
    Also accepts a community pot argument, but defaults this to 0."""

    def __init__(self, players: list, community_pot: int = 0):
        self.players = players
        self.community_pot = community_pot

    def pay_community_pot(self, player: Player, amount: int):
        """Pays into community pot for payments not directly to the bank."""
        player.money -= amount
        self.community_pot += amount
        print(f"{player.name} put ${amount} into the community pot.")

    def get_community_pot(self, player: Player):
        """Gives entire community pot to a player. Use this when a user lands on
        the 'free parking' space."""
        player.money += self.community_pot
        print(f"{player.name} earned ${self.community_pot} from the community pot.")
        self.community_pot = 0

def roll(self):
"""Roll dice for current player"""
    dice = {
        1: u"\u2680",
        2: u"\u2681",
        3: u"\u2682",
        4: u"\u2683",
        5: u"\u2684",
        6: u"\u2685",
    }
    roll_one = choice(list(dice.keys()))
    roll_two = choice(list(dice.keys()))
    print(dice.get(roll_one), "-", end=" ")
    print(dice.get(roll_two), "-", end=" ")
    print(roll_one + roll_two)
