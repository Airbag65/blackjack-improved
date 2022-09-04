import json
import random

class Card: 
    def __init__(self) -> None:
        self.suit = None
        self.value = None
        self.face_value = None
        self.suits = ["Hjärter", "Ruter", "Spader", "Klöver"]
        self.face_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.output = {
            "suit": "",
            "face_value": ""
        }


    def new_card(self) -> dict:
        self.suit = random.choice(self.suits)
        face_value = random.choice(self.face_values)
        if face_value == "J" or "Q" or "K" or "A":
            self.face_value = face_value
        else:
            self.face_value = str(face_value)
        self.output["suit"] = str(self.suit)
        self.output["face_value"] = str(self.face_value)
        json_card = json.dumps(self.output, indent=4)
        return self.output