import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("""SELECT * FROM user""")

results = cursor.fetchall()

print(results[0][0])
