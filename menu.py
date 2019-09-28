"""Menu to control the flow of the game."""

from time import sleep

from player import Player


class Menu:
    """Menu for interacting with players and game. Takes an initialized Game object as an
    argument(with initialized player objects) and begins the game."""

    def __init__(self, game):
        self.game = game

    def menu(self, player: Player):
        """Displays the top-level menu beginning each players turn."""
        print()
        while True:
            if player.is_bankrupt:
                return
            sleep(0.8)
            print(f"Community pot - ${self.game.community_pot}")
            for iplayer in self.game.players:
                print(f"{iplayer.name} - ${iplayer.money}", end="\t")
            print(f'\n{"=" * 75}')
            print(f"Current turn: {player.name} - ${player.money}\n")
            print("Choose an action:\n")
            print(
                "(R) Roll\n"
                "(P) Pay...\n"
                "(C) Collect money\n"
                "(G) Pass Go(collect $200)\n"
                "(E) End turn\n"
            )
            action = input("> ").lower()
            if action == "r":
                self.game.roll()
            elif action == "p":
                self.pay_menu(player)
                print()
            elif action == "c":
                self.collect_menu(player)
                print()
            elif action == "g":
                player.collect(amount=200)
            elif action == "e":
                break

    def pay_menu(self, player: Player):
        """Access this to determine who the current player will pay."""
        print(f'\n{"=" * 25}')
        amount = -1
        selected_player = None
        print("Choose who to pay:\n")
        print("(P) Pay Player\n" "(B) Pay Bank\n" "(C) Pay Community Pot\n" "(E) Pay Everyone\n")
        pay_action = input("> ").lower()
        if pay_action not in ["p", "b", "c", "e"]:
            print(f"({pay_action.upper()}) is not a value option.")
            return
        if pay_action == "p":
            selected_player = self.select_user_menu(player)
        while amount < 0:
            try:
                amount = int(input("How much?\n> "))
            except ValueError:
                print("Must select a numerical value")
        if selected_player:
            player.pay(amount, selected_player)
        elif pay_action == "b":
            player.pay(amount)
        elif pay_action == "c":
            self.game.pay_community_pot(player, amount)
        elif pay_action == "e":
            players = list(filter(lambda x: x != player, self.game.players))
            player.pay(amount, players)

    def collect_menu(self, player: Player):
        """Access this to determine from who the current player will collect money
        from."""
        print(f'\n{"=" * 25}')
        amount = -1
        print("Collect from:\n")
        print("(C) Community Pot\n" "(B) Bank\n" "(E) Everyone\n")
        collect_action = input("> ").lower()
        if collect_action not in ["c", "b", "e"]:
            print(f"({collect_action.upper()}) is not a value option.")
            return
        if collect_action == "c":
            amount = self.game.community_pot
            self.game.get_community_pot(player)
        while amount < 0:
            try:
                amount = int(input("How much?\n> "))
            except ValueError:
                print("Must select a numerical value")
        if collect_action == "b":
            player.collect(amount)
        elif collect_action == "e":
            players = list(filter(lambda x: x != player, self.game.players))
            player.collect(amount, players)

    def select_user_menu(self, player: Player):
        """Returns the Player object of the player whose name is typed in."""
        selected_player = None
        while not selected_player:
            try:
                print(f'\n{"=" * 25}')
                print("Select a player:\n")
                for other_player in self.game.players:
                    if other_player != player:
                        print(other_player.name)
                selected_name = input("> ").lower()
                selected_player = next(
                    filter(lambda x: x.name.lower() == selected_name, self.game.players)
                )
            except StopIteration:
                print()
                print("Could not find user.")
                sleep(0.8)
        return selected_player
