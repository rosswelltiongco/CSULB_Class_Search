# Make a database and mass insert rows of clases

import sqlite3 as sql
import scrape_classes as scraper

# Make database file, connection, and cursor
conn = sql.connect('current_semester.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Classes
             (Section ID, Class, Day, Time, Room, Professor)''')

# Get class information, then mass insert them into table
tables = scraper.getRooms()
c.executemany('INSERT INTO Classes VALUES (?,?,?,?,?,?)', tables)

# Save Changes
conn.commit()

# Close database connection
conn.close()
