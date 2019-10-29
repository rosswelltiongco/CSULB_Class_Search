import sqlite3 as sql

class Database:
    def __init__(self):
        pass


    def make_database(self, full_schedule):
        conn = sql.connect('current_semester.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE schedule
                    (CLASS_NUMBER, COURSE, DAYS, TIME, LOCATION, INSTRUCTOR)''')

        
        c.executemany('INSERT INTO schedule VALUES (?,?,?,?,?,?)', full_schedule)

        conn.commit()

        conn.close()


    def get_locations(self):
        conn = sql.connect('current_semester.db')
        c = conn.cursor()
        c.execute('''Select distinct location from schedule''')

        rows = c.fetchall()

        conn.commit()

        conn.close()

        return [self.format_location(location[0]) for location in rows]

    def format_location(self, location):
        location = location.strip("(')")
        location = location.rstrip("' ,)")
        return location


    def get_times(self, location):
        conn = sql.connect('current_semester.db')
        c = conn.cursor()
        c.execute('''select days, time from schedule where location is "{}"'''.format(location))

        rows = c.fetchall()

        conn.commit()

        conn.close()

        return [self.format_time(time) for time in rows]


    def format_time(self, time):
        
        day = time[0]
        time = time[1]

        #TuTh 8-8:50AM
        day.strip("(')")
        day.rstrip("',")
        time.strip("'")
        time.rstrip("')")
        
        return day + " " + time