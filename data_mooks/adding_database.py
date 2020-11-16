import sqlite3
import takingnames_from_website
import random

name_database = "database_1.db"

class connect:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def alter_table(self, table_name, column_name):
        self.cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} UNIQUE")
        self.connection.commit()
    def insert(self, table, col):
        self.cursor.execute(f"INSERT INTO {table} (imie,nazwisko,stopien_zaawansowania, ile_lat, adres_email) VALUES (?,?,?,?,?)", (col[0], col[1], col[2], col[3], col[4]))
        self.connection.commit()

    def print_column(self, table):
        return self.cursor.execute(f"SELECT * FROM {table}").description
    def search_data(self, table):
        return self.cursor.execute(f"SELECT * FROM {table} WHERE url LIKE www.google.p").fetchmany(4)


def list_check(list):
    if len(list) < 5:
        return "lista jest za krótka"
    elif len(list) > 5:
        return "lista jest za długa"
    else:
        return list


#tworzenie nowej tabeli
#connect(name_database).create_table('CREATE TABLE szkola (id INTEGER PRIMARY KEY AUTOINCREMENT, imie TEXT, nazwisko TEXT, stopien_zaawansowania TEXT, ile_lat INTEGER, adres_email NOT NULL UNIQUE)')


#tworzenie nowej kolumny na juz istniejącej tabeli
# try:
#    connect(name_database).alter_table('szkola', "adres_email2")
# except Exception as mer:
#    print(f"Nie można dodac nowej kolumny ponieważ: {mer}")
# #
# dodawanie nowego ucznia lista musi skladac sie z uczen = ["Marcin", "Zalewski", "zaaawanspowany", 8, "marcin_zalewski@gmail.com"]


def add_students():
    surnames = takingnames_from_website.list_of_surnames()
    names = takingnames_from_website.list_of_names()
    email = takingnames_from_website.list_of_emails()
    levele = takingnames_from_website.list_levels()
    for imie, nazwisko, email2 in zip(names, surnames, email):
        try:
            uczen = [imie, nazwisko, random.choice(levele),random.randint(18,65), email2]
            print(uczen)
            connect(name_database).insert('szkola', list_check(uczen))
            uczen = []
        except Exception as mer:
            print(f"Nie można dodać nowego ucznia ponieważ: {mer}")

# pobranie nazw kolumn z bazy:
# names = list(map(lambda x: x[0], connect(name_database).print_column('szkola')))
# print(names)
#print(connect(name_database).print_column('szkola'))
