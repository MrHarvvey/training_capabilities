from os import getenv
from dotenv import load_dotenv
import sqlite3
from sys import argv

load_dotenv()

print(getenv('DB_NAME'))

class connect:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(str)
        self.connection.commit()
    def insert(self, table, *values):
        self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()



print(argv)


if len(argv) > 2 and argv[1] == 'setup':
    print('tworze baze danych')
    # id imie nazwisko url
    db = connect(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, imie TEXT, url TEXT)')
    db.connection.commit()

#chce dodac python sql_lite.py add Oskar www.google.pl


if len(argv) == 4 and argv[1] == 'add':
    print('dodaje zmianne do bazy danych')
    imie = argv[2]
    url = argv[3]
    db = connect(getenv('DB_NAME'))
    db.insert('urls', None, imie, url)
