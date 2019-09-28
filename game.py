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
        dice = ["[*]", "[**]", "[***]", "[****]", "[*****]", "[******]"]
        roll_one = choice(dice)
        roll_two = choice(dice)
        print(roll_one, "-", end=" ")
        print(roll_two, "-", end=" ")
        print((len(roll_one) - 2) + (len(roll_two) - 2))
