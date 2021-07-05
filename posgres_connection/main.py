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
    fetched_object = None

    """Database connection """

    def __init__(self):

        self._con = psycopg2.connect(
            host="172.17.0.1",
            database="postgres",
            user="postgres",
            password="somePassword")

        # cursor
        self._cursor = self._con.cursor()

    """inserting Data into table mok_data"""

    def insert_data(self, age, email, name, surname, account_number):

        self._cursor.execute("insert into mok_data (age, email, name, surname, account_number) values (%s, %s, %s, %s, %s)", (age, email, name, surname, account_number))
        self._con.commit()


    def mok_times_data(self, value):
        for i in range(value):
            age = randint(23, 80)
            email = random.choice(self.random_emails)
            name = random.choice(self.random_names)
            surname = random.choice(self.random_surnames)

            account_number = ''.join(["{}".format(randint(0, 9)) for _ in range(0, 24)])
            self.insert_data(age, email, name, surname, account_number)
    def search_data(self):
        self._cursor.execute("select age, email, name, surname, account_number from mok_data where id = 5678")
        self.fetched_object = self._cursor.fetchall()



data = DatabaseMok()

#data.mok_times_data(120000)
data.search_data()
print(data.fetched_object)



