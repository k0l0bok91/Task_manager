import sqlite3
import json
from functools import wraps

class DataBaseStorage:
    """ Класс для сохранения в базе данных"""
    def __init__(self):
        self._create_db()
        self.db = sqlite3.connect("data_base.db")
        self.cursor = db.cursor()

    def commit_and_close(func):
        @wraps(func)
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            self.db.commit()
            self.db.close()
        return inner

    @commit_and_close
    def _create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS to_do_list(
            id INTEGER,
            task TEXT
                )""")

    @commit_and_close
    def add_task(self):

        self.cursor.execute("INSERT INTO to_do_list VALUES('01', 'test')")

DataBaseStorage.add_task(self)
