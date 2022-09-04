from .Card import Card
from .Player import Player
from .Dealer import Dealer
from .Database import Database
from pwinput import pwinput
from hashlib import md5
from termcolor import colored
import os
import time

class Game:
    def __init__(self, database_path: str, player: Player) -> None:
        self.player = player
        self.dealer = Dealer()
        self.db = Database(database_path)
        self.__menu()
    

    def __menu(self) -> None:
        print("--- Blackjack meny ---\n")
        saldo = colored(str(self.player.balance), "green")
        print(f"- Ditt tillgängliga saldo är {saldo} kr -")
        player_action = int(input("""Välj från anternativen nedan:
[1] Starta ny spelomgång
[2] Tillbaka
"""))
        if player_action == 1:
            os.system("cls" if os.name is "nt" else "clear")
            self.__new_round()
        elif player_action == 2:
            os.system("cls" if os.name is "nt" else "clear")
        else:
            os.system("cls" if os.name is "nt" else "clear")
            self.__menu()
        return


    def __new_round(self) -> None:
        print("--- Nytt spel ---\n")
        requested_bet = int(input("Ange hur mycket du vill satsa (Ange i heltal): "))
        round_over = False
        os.system("cls" if os.name == "nt" else "clear")
        print("--- Dina kort ---\n")
        self.player.draw_card()
        self.player.draw_card()
        for card in self.player.cards:
            print(self.player.cards[card]["suit"] + " " + self.player.cards[card]["face_value"])
        stop = input("")
        