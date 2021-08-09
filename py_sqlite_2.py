# py_sqlite_2.py

import sqlite3

with sqlite3.connect("saper.db") as connection:
	cursor = connection.cursor()

	# cursor.execute("DROP TABLE IF EXISTS users")
	cursor.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
	result = cursor.fetchall() # method for taking select result
	for result in cursor:
		print(result)

# connection.close()

'''
cursor.fetchmany(size) # fetch turples amount of size
cursor.fetchone() # fetch one turple
'''








