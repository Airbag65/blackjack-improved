from ast import Return
from .Card import Card
from .Player import Player
from .Dealer import Dealer
from .Database import Database
from pwinput import pwinput
from hashlib import md5

class Game:
    def __init__(self, database_path) -> None:
        self.player = None
        self.dealer = Dealer()
        self.db = Database(database_path)

    def __prompt_password(self) -> str:
        return md5(pwinput(prompt="Lösenord: ",mask="*").encode("utf-8")).hexdigest()

    def login(self) -> bool:
        entered_username = input("Användarnamn: ")
        try:
            account_info = self.db.fetch("get_user", entered_username)
        except:
            print(f"Inget konto med användarnamnet: '{entered_username}' kunde hittas")
            return False
        entered_password = self.__prompt_password()
        if entered_password == account_info["password"]:
            firstname = account_info["firstname"]
            print(f"Välkommen {firstname}!")
            return True
        else:
            print("Felaktigt lösenord!")
            
        