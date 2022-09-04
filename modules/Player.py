from .Card import Card
import json
import time

class Player:
    def __init__(self, username, password, email, first_name, last_name, balance) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.card_count = 1
        self.cards = {
            1: ""
            }
        
    def draw_card(self):
        card_module = Card()
        card = card_module.new_card()
        self.cards[self.card_count] = card
        self.card_count += 1
        