import sqlite3
import pandas as pd
import json

DB_DIR = "src\server-2\oust_database.db"
table_names = []
table_schemas = {}

conn = sqlite3.connect(DB_DIR)
cur = conn.cursor()

for element in cur.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall():
    table_names.append(element[0])

# Iterate through table names and collect schema of each table and store in dict
for table in table_names:
    schema_info = cur.execute(f"PRAGMA table_info({table})").fetchall()
    table_columns = []
    
    for column in schema_info:
            table_columns.append(f"Column: {column[1]}, Type: {column[2]}, Nullable: {column[3]}, Default: {column[4]}")
    
    table_schemas[table] = table_columns

for key in table_schemas:
            print(f"\nSchema for table: {key}")
            print("------------------------------------")
            for line in table_schemas.get(key):
                print(line)
