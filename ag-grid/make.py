import sqlite3 as sql

conn = sql.connect('current_semester.db')
c = conn.cursor()

c.execute('SELECT * FROM schedule') 


data = [row for row in c]

dictionary = {}

data_list = []

for row in data[:1000]:
    add_dictionary = {}
    add_dictionary["CLASS_NUMBER"] = row[0]
    add_dictionary["COURSE"] = row[1]
    add_dictionary["DAYS"] = row[2]
    add_dictionary["TIme"] = row[3]
    add_dictionary["start_date"] = row[4]
    add_dictionary["office"] = row[5]
    add_dictionary["extn"] = row[5]

    data_list.append(add_dictionary)

data_list = str(data_list)
data_list = data_list.replace("'",'"')

"""
    {
      "id": "4",
      "name": "Cedric Kelly",
      "position": "Senior Javascript Developer",
      "salary": "$433,060",
      "start_date": "2012/03/29",
      "office": "Edinburgh",
      "extn": "6224"
    },
"""

conn.commit()

conn.close()

with open('somefile.txt', 'w') as the_file:
    the_file.write(data_list)
