class Player:
    def __init__(self, username, password, first_name, last_name, balance) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.cards = list("")