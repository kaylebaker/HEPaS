import sqlite3

DB_DIR = "C:\\Users\\krbak\OneDrive\\Uni\\Year 3 Semester 1\\CSI3344 Distributed Systems\\Assignment 3\\Code\\HEPaS\\src\\server-2\\oust_database.db"

conn = sqlite3.connect(DB_DIR)
cur = conn.cursor()

for record in cur.execute('SELECT * FROM Students'):
    print(record)
