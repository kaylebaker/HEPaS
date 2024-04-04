import sqlite3

# Create SQL connection to SQLite database
conn = sqlite3.connect("Code\Database\oust_database.db")

# Create cursor object to perform SQL operations
cur = conn.cursor()

# execute() performs a single SQL statement
for row in cur.execute('SELECT * FROM students'):
    print(row)

# Close the connection
conn.close()