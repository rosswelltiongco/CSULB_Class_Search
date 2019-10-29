import calendar
import datetime


class Time:
    
    def __init__(self):
        import os, time
        time.strftime('%X %x %Z')
        os.environ['TZ'] = 'US/Pacific'
        # time.tzset()

        self.day = self.get_today()
        self.time = self.get_current_time()


    def set_day(self, new_day):
        self.day = new_day


    def set_time(self, new_time):
        self.time = new_time


    def get_day(self):
        return self.day


    def get_time(self):
        return self.time


    def get_today(self):
        from datetime import date
        import calendar
        my_date = date.today()
        today = calendar.day_name[my_date.weekday()]

        # Shortening logic
        if today == "Monday":
            today = "M"
        elif today == "Tuesday":
            today = "Tu"
        elif today == "Wednesday":
            today = "W"
        elif today == "Thursday":
            today = "Th"
        elif today == "Friday":
            today = "F"
        elif today == "Saturday":
            today = "Sa"
        else:
            today = "Su"

        return today


    def get_current_time(self):
        import datetime
        currentDT = datetime.datetime.now()

        # Military time
        currenttime = str(currentDT.hour) + ":" + str(currentDT.minute)
        hour = currentDT.hour
        minute = currentDT.minute

        return self.mins_since_midnight(hour, minute)
        

    def mins_since_midnight(self, hour, minute):
        # Minutes passed since midnight
        minutesSinceMidnight = hour*60 + minute
        return minutesSinceMidnight # To take into account repl's time

    def convert_time(self, time):
        # There are three main cases and some transitional edge cases
        morningCase = 'TuTh 10:30-11:45AM' #Morning - Convert both times normally
        afternoonCase = 'TuTh 12-1:15PM' #Afternoon - Convert second time to have 12 more hours
        eveningCase = 'TuTh 6-6:50PM' #Night - Convert both times to have 12 more hours
        edgeCase1 = 'MW 10-2:15PM'
        edgeCase2 = 'MW 11-12:15PM'
        edgeCase3 = "MW 12-3:00PM"

        # Example: time = 'TuTh 12-1:15PM'
        timeRange = time.split()[1] # 12-1:15PM
        firstTime = timeRange.split("-")[0] # 12
        secondTime = timeRange.split("-")[1] # 1:15PM

        # Populating 00 for convenience
        if ":" not in firstTime:
            firstTime+=":00"
        if ":" not in secondTime:
            secondTime+=":00"

        firstHour = int(firstTime.split(":")[0])
        firstMinutes = int(firstTime.split(":")[1][:2])
        secondHour = int(secondTime.split(":")[0])
        secondMinutes = int(secondTime.split(":")[1][:2])

        convertedSecondTime = secondHour * 60 + secondMinutes
        if "PM" in secondTime:
            convertedSecondTime+=720
        if convertedSecondTime >= 1440:
            convertedSecondTime-=720

        convertedFirstTime = firstHour * 60 + firstMinutes
        if "PM" in secondTime:
            convertedFirstTime+=720
        if convertedFirstTime >= 1440:
            convertedFirstTime-=720
        if convertedFirstTime > convertedSecondTime:
            convertedFirstTime -=720

        converted = str(convertedFirstTime) + "-" + str(convertedSecondTime)
        return converted


    testList = ['TuTh 10:30-11:45AM', 'MW 4-5:15PM', 'TuTh 8:30-9:45PM', 'TuTh 9-10:15AM', 'TuTh 12-1:15PM', 'MW 6-7:15PM', 'TuTh 6-6:50PM', 'TuTh 7-8:15PM', 'MW 1-1:50PM', 'MW 2-3:15PM', 'MW 10-11:15AM', 'M 7:30-8:20PM']

    # Returns how long class is open
    # If positive, it is open
    # If negative, it is closed
    def minutesLeft(self, classroomTimes):
        today = self.get_today()
        currentTime = self.get_current_time()
        minutesLeft = 999999
        for time in classroomTimes:
            if today in time[:-2]: #Strips AM/PM for monday
                startTime = self.convert_time(time).split('-')[0]
                endTime  = self.convert_time(time).split('-')[1]
                if int(startTime) < currentTime < int(endTime):
                    minutesLeft = int(endTime)-currentTime
                    return -minutesLeft
                newTimeLeft = int(startTime) - currentTime
                if (newTimeLeft < minutesLeft) and (newTimeLeft > 0):
                    minutesLeft = newTimeLeft
        # If none of the times are used by either day or time, it is open
        return minutesLeft

    ecs412 = ["TuTh 8-8:50AM", "TuTh 9-10:15AM", "MW 6-7:15PM", "F 3-5:30PM", "MW 9-10:15AM", "MW 12-1:15PM", "TuTh 10:30-11:45AM", "F 11-1:30PM", "TuTh 12-1:15PM", "MW 8:30-9:45PM", "MW 4-5:15PM", "TuTh 1:30-2:45PM", "TuTh 7-8:15PM", "TuTh 7-8:15PM"]
    ecs416 = ["TuTh 1:30-2:45PM", "MW 11-12:15PM", "F 12-2:30PM", "MW 3-3:50PM", "MW 4-5:15PM", "TuTh 3-4:15PM", "TuTh 3-4:15PM", "TuTh 10:30-11:45AM", "TuTh 6-7:15PM", "MW 7:30-8:45PM", "TuTh 4:30-5:45PM", "TuTh 4:30-5:45PM", "TuTh 12-1:15PM", "MW 6-7:15PM", "TuTh 9-10:15AM", "TuTh 7:30-8:45PM", "TuTh 7:30-8:45PM"]


ecs412 = ["TuTh 8-8:50AM", "TuTh 9-10:15AM", "MW 6-7:15PM", "F 3-5:30PM", "MW 9-10:15AM", "MW 12-1:15PM", "TuTh 10:30-11:45AM", "F 11-1:30PM", "TuTh 12-1:15PM", "MW 8:30-9:45PM", "MW 4-5:15PM", "TuTh 1:30-2:45PM", "TuTh 7-8:15PM", "TuTh 7-8:15PM"]
# ecs416 = ["TuTh 1:30-2:45PM", "MW 11-12:15PM", "F 12-2:30PM", "MW 3-3:50PM", "MW 4-5:15PM", "TuTh 3-4:15PM", "TuTh 3-4:15PM", "TuTh 10:30-11:45AM", "TuTh 6-7:15PM", "MW 7:30-8:45PM", "TuTh 4:30-5:45PM", "TuTh 4:30-5:45PM", "TuTh 12-1:15PM", "MW 6-7:15PM", "TuTh 9-10:15AM", "TuTh 7:30-8:45PM", "TuTh 7:30-8:45PM"]

from Database import *
database = Database()
vec420 = database.get_times("VEC-420")

"""
time = Time()
x = time.minutesLeft(ecs412)
print(x)

y = time.minutesLeft(vec420)
print(y)
"""