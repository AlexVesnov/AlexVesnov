# py_sqlite_4.py

import sqlite3

def readAva(n):
    try:
        with open(f"avas/{n}.png", "rb") as f: # для работы необходим каталог с аватарками
            return f.read()

    except IOError as e:
        print(e)
        return False

with sqlite3.connect("cars.db") as connection:

	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	# cursor.execute("DROP TABLE IF EXISTS cars")
	cursor.executescript("""CREATE TABLE IF NOT EXISTS users (
		name TEXT,
        ava BLOB,
		score INTEGER
	)""")




