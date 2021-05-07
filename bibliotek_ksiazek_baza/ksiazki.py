import sqlite3

#conn = sqlite3.connect(':memory:')   -  for memory database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# c.execute("""CREATE TABLE students (
#             first text,


#             last text,
#             id integer,
#             email text
#             )""")
#

conn.commit()

conn.close()

