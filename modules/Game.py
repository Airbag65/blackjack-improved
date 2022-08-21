from .Card import Card
from .Player import Player
from .Dealer import Dealer
from .Database import Database
from pwinput import pwinput
from hashlib import md5
import os

class Game:
    def __init__(self, database_path) -> None:
        self.player = None
        self.dealer = Dealer()
        self.db = Database(database_path)
        


    