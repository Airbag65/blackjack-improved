from .query import fetch
import sqlite3

class Database:
    def __init__(self, database_path) -> None:
        self.con = sqlite3.connect(database_path)
        self.cur = self.con.cursor()

    def fetch(self, query_string, username) -> dict:
        query = fetch[query_string].format(username = username)
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

