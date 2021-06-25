import psycopg2

class InsertData:
    # connect to the db
    _cursor = None
    def __init__(self):
        self._con = psycopg2.connect(
            host="172.17.0.1",
            database="oskar_test",
            user="postgres",
            password="somePassword")

        # cursor
        self._cursor = self._con.cursor()

    def __call__(self, nr_rachunku, wlasciciel_rachunku, saldo, waluta):
        self._cursor.execute("insert into rachunki_bankowe (nr_rachunku, wlasciciel_rachunku, saldo, waluta) values (%s, %s, %s, %s)", (nr_rachunku, wlasciciel_rachunku, saldo, waluta))
        self._con.commit()
        self._con.close()

data = InsertData()

data(12321312214321423233, 'Monika', 4.6, 2)




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
