import sqlite3

with sqlite3.connect("saper.db") as connection:
	cursor = connection.cursor()

	# cursor.execute("DROP TABLE IF EXISTS users")
	cursor.execute("""CREATE TABLE IF NOT EXISTS users (
		user_id PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		sex INTEGER NOT NULL DEFAULT 1,
		old INTEGER,
		score INTEGER)""")

# connection.close()
# some comment
# another consistent comment


