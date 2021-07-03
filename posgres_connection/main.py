import psycopg2
import random
from random import randint


class DatabaseMok:
    random_names = ['Julia', 'Marc', 'Stanisław', 'Oskar', 'Monika', 'Andzelika', 'Jurek', 'Wlodek', 'Kadzyslaw',
                    'Wemiar']
    random_surnames = ['Kowalski', 'Smith', 'Roberts', 'Kazmierczak', 'Zych', 'Wojciechowski', 'Marciniak']
    random_emails = ['wertyak@wp.pl', 'sandy22@gmail.com', 'tantykat34@hotmail.com', 'bertat34@hotmail.com',
                     'erntykat34@hotmail.com']
    # connect to the db
    _cursor = None

    def __init__(self):
        self._con = psycopg2.connect(
            host="172.17.0.1",
            database="postgres",
            user="postgres",
            password="somePassword")

        # cursor
        self._cursor = self._con.cursor()

    def insert_data(self, age, email, name, surname, account_number):

        self._cursor.execute("insert into mok_data (age, email, name, surname, account_number) values (%s, %s, %s, %s, %s)", (age, email, name, surname, account_number))
        self._con.commit()
        #self._con.close()

    def __del__(self):
        self._cursor = self._con.cursor()

    def search_data(self):
        self._cursor.execute("select * from mok_data ")
        self._cursor.fetchall()

    def mok_times_data(self, value):
        for i in range(value):
            age = randint(23, 80)
            email = random.choice(self.random_emails)
            name = random.choice(self.random_names)
            surname = random.choice(self.random_surnames)

            account_number = ''.join(["{}".format(randint(0, 9)) for _ in range(0, 24)])
            self.insert_data(age, email, name, surname, account_number)

data = DatabaseMok()

data.mok_times_data(120000)







#mok_times_data(100000)



# cur.execute("insert into rachunki_bankowe (nr_rachunku, wlasciciel_rachunku, saldo, waluta) values (%s, %s, %s, %s)", ('2323232323232623232323234', "Hussein", 323, 2))
#
# #execute query
# cur.execute("select * from rachunki_bankowe")
#
# rows = cur.fetchall()
#
# for r in rows:
#     print(f"id {r[0]} name {r[1]}")
#
# #commit the transcation
# con.commit()
#
# #close the cursor
# cur.close()

#close the connection
