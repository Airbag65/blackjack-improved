from .Card import Card
from .Player import Player
from .Dealer import Dealer

class Game:
    def __init__(self, username, password, first_name, last_name, balance) -> None:
        self.player = Player(username, password, first_name, last_name, balance)
        self.dealer = Dealer()
