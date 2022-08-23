from pwinput import pwinput
from hashlib import md5
import os
from termcolor import colored
from modules.Game import Game
from .Card import Card
from .Player import Player
from .Dealer import Dealer
from .Database import Database
import time


class Menu:
    def __init__(self, database_path) -> None:
        self.game = Game(database_path)
        self.__start_page()

    def __quit(self):
        print("--- Välkommen åter ---\n")

    def __prompt_password(self) -> str:
        return md5(pwinput(prompt="Lösenord: ",mask="*").encode("utf-8")).hexdigest()

    def __login(self) -> bool:
        print("--- Logga in ---\n")
        entered_username = input("Användarnamn: ")
        try:
            account_info = self.game.db.fetch("get_username", entered_username)
        except:
            print(f"Inget konto med användarnamnet: '{entered_username}' kunde hittas")
            return False
        entered_password = self.__prompt_password()
        if entered_password == account_info["password"]:
            self.player = Player(
                account_info["username"],
                account_info["password"],
                account_info["email"],
                account_info["firstname"],
                account_info["lastname"],
                account_info["balance"])
            self.__landing_page()
            return True
        else:
            print("Felaktigt lösenord!")
            
    def __new_account(self) -> bool:
        print("--- Skapa nytt konto ---\n")
        entered_username = input("Användarnamn: ")
        try:
            if self.game.db.fetch("get_username", entered_username)["username"] == entered_username:
                print("Användarnamnet är upptaget!")
                self.__new_account()
                return False
        except:
            pass
        entered_email = input("E-postadress: ")
        try:
            if self.game.db.fetch("get_email", entered_email)["email"] == entered_email:
                print("Ett konto är redan anslutet till denna e-postadress!")
                self.__new_account()
                return False
        except:
            pass
        entered_firstname = input("Förnamn: ")
        entered_lastname = input("Efternamn: ")
        entered_password = self.__prompt_password()
        print("Ange lösenordet igen")
        entered_confirm_password = self.__prompt_password()
        if entered_password == entered_confirm_password:
            self.game.db.add(
                "new_user",
                entered_username,
                entered_email,
                entered_firstname,
                entered_lastname,
                entered_password)
            self.player = Player(
                entered_username,
                entered_password,
                entered_email,
                entered_firstname,
                entered_lastname,
                0)
            self.__landing_page()
            return True
        else:
            print("Lösenorden är inte likadana! \nFörsök igen!\n")
            return False
        
    def __start_page(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print("--- Välkommen till Blackjack ---\n")
        player_action = int(input("""Välj från alternativen nedan:
[0] Logga in 
[1] Skapa konto
[2] Avsluta
"""))
        if player_action == 0:
            os.system("cls" if os.name == "nt" else "clear")
            self.__login()
        elif player_action == 1:
            os.system("cls" if os.name == "nt" else "clear")
            self.__new_account()
        elif player_action == 2:
            os.system("cls" if os.name == "nt" else "clear")
            self.__quit()
        else:
            self.__start_page()
    
    def __landing_page(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"--- Välkommen {self.player.first_name} ---\n")
        player_action = int(input("""Välj från alternativen nedan:
[0] Spela Blackjack
[1] Mitt konto
[2] Plånbok
[3] Avsluta
"""))
        if player_action == 0:
            os.system("cls" if os.name == "nt" else "clear")
            self.__quit()
        elif player_action == 1:
            os.system("cls" if os.name == "nt" else "clear")
            self.__view_account()
        elif player_action == 2:
            os.system("cls" if os.name == "nt" else "clear")
            self.__wallet()
        elif player_action == 3:
            os.system("cls" if os.name == "nt" else "clear")
            self.__quit()
        else:
            self.__landing_page()

    def __wallet(self) -> None:
        saldo = colored(self.player.balance, "green")
        print(f"--- Plånbok ---\n\nDitt saldo är {saldo} kr\n\n")
        player_action = int(input("""Välj från alternativen nedan: 
[0] Insättning (Ej implementerad ännu)
[1] Uttag (Ej implementerad ännu)
[2] Tillbaka
"""))
        if player_action == 0:
            os.system("cls" if os.name == "nt" else "clear")
            self.__landing_page()
        if player_action == 1:
            os.system("cls" if os.name == "nt" else "clear")
            self.__landing_page()
        if player_action == 2:
            os.system("cls" if os.name == "nt" else "clear")
            self.__landing_page()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            self.__wallet()

    def __view_account(self) -> None:
        player_balance = colored(self.player.balance, "green")
        print(f"--- Mitt konto ---\n\n-- {self.player.first_name} {self.player.last_name} --")
        to_print = [f"Användarnamn: {self.player.username}", 
                    f"E-postadress: {self.player.email}",
                    f"Saldo: {player_balance} kr"]
        for item in to_print:
            print(item)
        player_action = int(input("""Välj från alternativen nedan:
[0] Ändra användarnamn 
[1] Ändra e-postadress 
[2] Ändra lösenord 
[3] Tillbaka
"""))   
        if player_action == 0:
            os.system("cls" if os.name == "nt" else "clear")
            self.__change_username()
        elif player_action == 1:
            os.system("cls" if os.name == "nt" else "clear")
            self.__change_email()
        elif player_action == 2:
            os.system("cls" if os.name == "nt" else "clear")
            self.__change_password()
        elif player_action == 3:
            os.system("cls" if os.name == "nt" else "clear")
            self.__landing_page()   
        return
        
    def __change_username(self) -> None:
        print("--- Byt användarnamn ---\n")
        new_username = input("Ange ditt nya användarnamn: ")
        try:
            self.game.db.update("update_username", new_username, self.player.email)
            self.player.username = new_username
            print("\nAnvändarnamnet uppdaterat!")
            time.sleep(2)
            os.system("cls" if os.name is "nt" else "clear")
            self.__view_account()
        except:
            print("\nMisslyckades...")
            time.sleep(2)
            self.__view_account()
        return

    def __change_email(self) -> None:
        print("--- Ändra ansluten e-portadress ---\n")
        new_email = input("Ange din nya e-portadress: ")
        try:
            self.game.db.update("update_email", new_email, self.player.username)
            self.player.email = new_email
            print("\nE-postadressen uppdaterat!")
            time.sleep(2)
            os.system("cls" if os.name is "nt" else "clear")
            self.__view_account()
        except:
            print("\nMisslyckades...")
            time.sleep(2)
            self.__view_account()
        return

    def __change_password(self) -> None:
        print("--- Ändra lösenord ---\n")
        print("Ange ditt nya lösenord")
        new_password = self.__prompt_password()
        print("Upprepa ditt nya lösenord")
        confirm_new_password = self.__prompt_password()
        if new_password == confirm_new_password:
            try:
                self.game.db.update("update_password", new_password, self.player.username)
                self.player.password = new_password
                print("\nLösenordet uppdaterat!")
                time.sleep(2)
                os.system("cls" if os.name is "nt" else "clear")
                self.__view_account()
            except:
                print("\nMisslyckades...")
                time.sleep(3)
                self.__view_account()
        else:
            print("\nLösenorden matchar inte! \nVälj 'Ändra lösenord' och försök igen")
            time.sleep(2)
            os.system("cls" if os.name is "nt" else "clear")
            self.__view_account()
        return
            