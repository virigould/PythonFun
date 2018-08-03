import sqlite3

# database practice with python.

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("""DROP TABLE user""")

command = """
CREATE TABLE user (
uname VARCHAR(15),
walletAmount INTEGER,
joining DATE);"""

cursor.execute(command)

command = """INSERT INTO user (uname, walletAmount, joining)
                VALUES ("Test User", 100, 2018-07-12);"""

cursor.execute(command)

connection.commit()


connection.close()
