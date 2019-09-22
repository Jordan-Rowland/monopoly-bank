from itertools import cycle

class Game:
    def __init__(self, players):
        self.players = players
        self.community_pot = 0
#        self.history = [] 

    def pay_community_pot(self, player, amount):
        player.money -= amount
        self.community_pot += amount
        print(f'{player.name} put ${amount} into the community pot.')

    def get_community_pot(self, player):
        player.money += self.community_pot
        print(f'{player.name} earned ${self.community_pot} from the community pot.')
        self.community_pot = 0

    def menu(self, player):
        print()
        for player in self.players:
            print(f'{player.name} - ${player.money}', end='\t')
        print(f'\n{"=" * 75}')
        print(f'Current turn: {player.name} - ${player.money}\n')
        print(
            "Choose an action:\n"
            "(P) Pay...\n"
            "(C) Collect money\n"
            "(E) End turn\n"
        )
        action = input('> ').lower()
        if action == 'p':
            self.pay_menu(player)
        elif action == 'c':
            pass
        elif action == 'e':
            pass

    def pay_menu(self, player):
        print(f'\n{"=" * 25}')
        amount = None
        while not amount:
            try:
                amount = int(input('How much?\n> '))
            except ValueError:
                print('Must select a numerical value')
        print('Choose who to pay:\n')
        print(
            "(P) Pay Player\n"
            "(B) Pay Bank\n"
            "(C) Pay Community Pot\n"
            "(E) Pay Everyone"
        )
        pay_action = input('> ').lower()
        if pay_action == 'b':
            player.pay_bank(amount)
        elif pay_action == 'c':
            self.pay_community_pot(player, amount)
        elif pay_action == 'p':
            selected_player = self.select_user_menu(player)
            player.pay_player(selected_player, amount)
        elif pay_action == 'e':
            player.pay_all_players(self.players, amount)

    def select_user_menu(self, player):
        print(f'\n{"=" * 25}')
        print('Select a player:\n')
        for other_player in self.players:
            if other_player != player:
                print(other_player.name)
        selected_name = input('> ').lower()
        selected_player = [player for player in game.players
                            if player.name.lower() == selected_name][0]
        return selected_player
        

class Player:
    """Player class, handles state regarding money, name, and properties."""
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.is_bankrupt = False

    def pay_player(self, player, amount):
        self.money -= amount
        player.money += amount
        print(f'{self.name} paid {player.name} ${amount}.')

    def pay_bank(self, amount):
        self.money -= amount
        print(f'{self.name} paid the bank ${amount}.')

    def receive_money(self, amount):
        self.money += amount
        print(f'{self.name} received ${amount}.')
    
    def receive_from_players(self, players, amount):
        for player in players:
            player.pay_player(self, amount)

    def pay_all_players(self, players, amount):
        for player in players:
            self.pay_player(player, amount)


#if __name__ == '__main__':
p1 = Player('Rick')
p2 = Player('Jim')
p3 = Player('Dave')
game = Game([p1, p2, p3])
for i in game.players:
    game.menu(i)
