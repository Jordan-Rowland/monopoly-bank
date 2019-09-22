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


class Player:
    """Player class, handles state regarding money, name, and properties."""
    def __init__(self, name):
        self.name = name
        self.money = 1500
#        self.properties = []

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


p1 = Player('Steve')
p2 = Player('Dave')
p3 = Player('Kathy')
game = Game([p1, p2, p3])

p1.pay_player(p2, 100)
print(p1.name, p1.money)
print(p2.name, p2.money)

print()
p1.pay_bank(100)
print(p1.name, p1.money)

print()
p1.receive_money(100)
print(p1.name, p1.money)

print()
p1.receive_from_players([p2, p3], 30)
print(p1.name, p1.money)
print(p2.name, p2.money)

print()
game.pay_community_pot(p3, 50)
game.get_community_pot(p1)
