import sqlite3

from mpmath.matrices.matrices import rowsep

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("SELECT * FROM users")
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()