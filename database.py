import sqlite3
import scraper
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE classes
             (id, name, day, time, room, professor)''')

# Insert a row of data
tables = scraper.getRooms()
# for row in tables:
#     c.execute("INSERT INTO classes VALUES ('{}','{}','{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3],row[4],row[5]))
c.executemany('INSERT INTO classes VALUES (?,?,?,?,?,?)', tables)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
