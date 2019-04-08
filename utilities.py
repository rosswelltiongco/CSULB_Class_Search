

def get_today():
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


def get_current_time():
    import datetime
    currentDT = datetime.datetime.now()

    # Military time
    currenttime = str(currentDT.hour) + ":" + str(currentDT.minute)

    # Minutes passed since midnight
    minutesSinceMidnight = currentDT.hour*60 + currentDT.minute
    return minutesSinceMidnight




def convert_time(time):
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
def minutesLeft(classroomTimes):
    today = get_today()
    currentTime = get_current_time()
    minutesLeft = 999999
    for time in classroomTimes:
        if today in time[:-2]: #Strips AM/PM for monday
            startTime = convert_time(time).split('-')[0]
            endTime = convert_time(time).split('-')[1]
            if int(startTime) < currentTime < int(endTime):
                minutesLeft = int(endTime)-currentTime
                return -minutesLeft
            newTimeLeft = int(startTime) - currentTime
            if (newTimeLeft < minutesLeft) and (newTimeLeft > 0):
                minutesLeft = newTimeLeft
    # If none of the times are used by either day or time, it is open
    return minutesLeft

"""
NOTES
"""


"""
days can be stored in 14 combinations
"MW"
"TuTh"
"M"
"TBA"
"Tu"
"W"
"Th"
"Sa"
"F"
"MWF"
"SaSu"
"TuThF"
"MTuWTh"
"MTuWThF"
"""
