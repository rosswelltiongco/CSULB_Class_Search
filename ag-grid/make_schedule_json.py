import sqlite3 as sql
import json

def get_locations():
        conn = sql.connect('current_semester.db')
        c = conn.cursor()
        c.execute('''Select distinct location from schedule''')

        rows = c.fetchall()

        conn.commit()

        conn.close()

        return [format_location(location[0]) for location in rows]

def format_location(location):
    location = location.strip("(')")
    location = location.rstrip("' ,)")
    return location


def get_times(location):
    conn = sql.connect('current_semester.db')
    c = conn.cursor()
    c.execute('''select days, time from schedule where location is "{}"'''.format(location))

    rows = c.fetchall()

    conn.commit()

    conn.close()

    return [format_time(time) for time in rows]


def format_time(time):
    
    day = time[0]
    time = time[1]

    #TuTh 8-8:50AM
    day.strip("(')")
    day.rstrip("',")
    time.strip("'")
    time.rstrip("')")
    
    return day + " " + time

def get_schedule( json_str = False ):
    schedule = {}
    for location in get_locations():
        schedule[location] = get_times(location)


    if json_str:
        return json.dumps(schedule) #CREATE JSON



with open('schedule_data.json', 'w') as the_file:
    the_file.write(get_schedule( json_str = True ))
