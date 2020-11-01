import sqlite3

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

    def alter_table(self, table_name, imie, nazwisko, stopien_zaawansowania, ile_lat, adred_email):
        self.cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} TEXT")
        self.connection.commit()
    def insert(self, table, col):
            self.cursor.execute(f"INSERT INTO {table} (imie,nazwisko,stopien_zaawansowania, ile_lat, adres_email) VALUES (?,?,?,?,?)", (col[0], col[1], col[2], col[3], col[4]))
            self.connection.commit()
    def print_column(self,table):
        return self.cursor.execute(f"SELECT * FROM {table}"),
    def search_data(self, table):

        return self.cursor.execute(f"SELECT * FROM {table} WHERE url LIKE www.google.p").fetchmany(4)

#tworzenie nowej tableli
#connect(name_database).create_table('CREATE TABLE szkola (id INTEGER PRIMARY KEY AUTOINCREMENT, imie TEXT, nazwisko TEXT, stopien_zaawansowania TEXT, ile_lat INTEGER)')


#tworzenie nowej kolumny na juz istniejącej tabeli
#try:
#    connect(name_database).alter_table('szkola', "adres_email")
#except Exception as mer:
#    print(f"Nie można dodac nowej kolumny ponieważ: {mer}")

# dodawanie nowego ucznia lista musi skladac sie z uczen = ["Marcin", "Zalewski", "zaaawanspowany", 8, "marcin_zalewski@gmail.com"]

# uczen = ["Marcin", "Zalewski", "zaaawanspowany", 8, "marcin_zalewski@gmail.com"]
# try:
#     connect(name_database).insert('szkola', uczen)
# except Exception as mer:
#     print(f"Nie można dodać nowego ucznia ponieważ: {mer}")


print(connect(name_database).print_column('szkola'))