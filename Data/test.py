import sqlite3

conn = sqlite3.connect('ds.db')
cursor = conn.cursor()

# Retrieve all data from the 'distances' table
cursor.execute('SELECT * FROM distances')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
