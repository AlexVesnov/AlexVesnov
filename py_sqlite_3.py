# py_sqlite_3.py

import sqlite3

cars = [
	('Audi', 52642),
	('Mersedes', 57127),
	('Skoda', 9000),
	('Volvo', 29000),
	('Bentley', 350000)
]

with sqlite3.connect("cars.db") as connection:
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	# cursor.execute("DROP TABLE IF EXISTS cars")
	cursor.executescript("""CREATE TABLE IF NOT EXISTS cars (
		car_id INTEGER PRIMARY KEY AUTOINCREMENT,
		model TEXT,
		price INTEGER
	)""")

	# for car in cars:
	# 	cursor.execute("INSERT INTO cars VALUES(NULL, ?, ?)", cars[0])

	# cursor.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars) # alternatively
	cursor.execute("SELECT model, price FROM cars")
	# rows = cursor.fetchall()
	# print(rows)
	for result in cursor:
		print(result['model'], result['price'])

	# connection.commit()
	# connection.close() # apply autonatically




