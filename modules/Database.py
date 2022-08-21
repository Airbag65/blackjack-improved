from .query import fetch, add
import sqlite3

class Database:
    def __init__(self, database_path) -> None:
        self.con = sqlite3.connect(database_path)
        self.cur = self.con.cursor()

    def fetch(self, query_string, prompt) -> dict:
        query = fetch[query_string].format(prompt=prompt)
        self.cur.execute(query)
        fetched_data = list(self.cur.fetchall()[0])
        data = {
            "id": fetched_data[0],
            "username": fetched_data[1],
            "email": fetched_data[2],
            "firstname": fetched_data[3],
            "lastname": fetched_data[4],
            "balance": fetched_data[5],
            "password": fetched_data[6]
        }
        return data

    def add(self, query_string, username, email, firstname, lastname, password) -> bool:
        query = add[query_string].format(
            username=username,
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password)
        try:
            self.cur.execute(query)
            self.con.commit()
        except:
            print("Något gick fel!")
            return False
        print("Kontot skapat!")
        return True
