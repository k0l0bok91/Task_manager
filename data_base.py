import sqlite3
import json
from functools import wraps




class DataBaseStorage:
    """ Класс для сохранения словаря в базе данных"""
    def __init__(self, db, cursor):
        self._create_db()
        db = sqlite3.connect("data_base.db")
        cursor = db.cursor()
        # self.db = db
        # self.cursor = cursor

    def _commit_and_close(self):
        db.commit()
        db.close()

    def _create_db(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS to_do_list(
            id INTEGER,
            task TEXT
                )""")
        self._commit_and_close()

    def add_task(self):
        db = sqlite3.connect("data_base.db")
        cursor.execute("INSERT INTO to_do_list VALUES('01', 'test')")
        self._commit_and_close()

db_storage = DataBaseStorage(db, cursor)
db_storage.add_task()
