from modules.Player import Player
from modules.Game import Game
from modules.Database import Database

if __name__ == "__main__":
    g = Game("database/database.sqlite")
    g.login()