import sqlite3

DB_DIR = "src\server-2\database\oust_database.db"


# Establish connection to SQLite database and create cursor object to perform SQL operations
conn = sqlite3.connect(DB_DIR)
cur = conn.cursor()

for row in cur.execute('SELECT * FROM Students LIMIT 5'):
    print(row)