from ast import Return
from xmlrpc.client import boolean
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
            account_info = self.db.fetch("get_username", entered_username)
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
            
    def new_account(self) -> bool:
        print("--- SKAPA NYTT KONTO ---")
        entered_username = input("Användarnamn: ")
        try:
            if self.db.fetch("get_username", entered_username)["username"] == entered_username:
                print("Användarnamnet är upptaget!")
                return False
        except:
            pass
        entered_email = input("E-postadress: ")
        try:
            if self.db.fetch("get_email", entered_email)["email"] == entered_email:
                print("Ett konto är redan anslutet till denna e-postadress!")
                return False
        except:
            pass
        entered_firstname = input("Förnamn: ")
        entered_lastname = input("Efternamn: ")
        entered_password = self.__prompt_password()
        print("Ange lösenordet igen")
        entered_confirm_password = self.__prompt_password()
        if entered_password == entered_confirm_password:
            self.db.add(
                "new_user",
                entered_username,
                entered_email,
                entered_firstname,
                entered_lastname,
                entered_password)
            return True
        else:
            print("Lösenorden är inte likadana!")
            return False
        