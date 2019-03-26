

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
    # There are three possible cases
    morningCase = 'TuTh 10:30-11:45AM' #Morning - Convert both times normally
    afternoonCase = 'TuTh 12-1:15PM' #Afternoon - Convert second time to have 12 more hours
    eveningCase = 'TuTh 6-6:50PM' #Night - Convert both times to have 12 more hours

    # Example: time = 'TuTh 12-1:15PM'
    timeRange = time.split()[1] # 12-1:15PM
    firstTime = timeRange.split("-")[0] # 12
    secondTime = timeRange.split("-")[1] # 1:15PM

    # Populating 00 for convenience
    if ":" not in firstTime:
        firstTime+=":00"
    if ":" not in secondTime:
        secondTime+=":00"

    firstHour = firstTime.split(":")[0]
    firstMinutes = firstTime.split(":")[1][:2]
    secondHour = secondTime.split(":")[0]
    secondMinutes = secondTime.split(":")[1][:2]
    # Determing if morning, afternoon, or evening
    if "PM" in secondTime:
        # Evening case
        if (firstHour*60+firstMinutes < secondHour*60+secondMinutes):
            firstTime+="PM"
        # Afternoon case
        else:
            firstTime+="AM"
    # Morning case
    else:
        firstTime+="AM"

    # Converting to minutes passed since midnight
    convertedFirst = int(firstHour)*60+int(firstMinutes)
    convertedSecond = int(secondHour)*60+int(secondMinutes)

    # # Adding time if PM
    if "PM" in str(firstTime):
        convertedFirst+=(12*60)
    if "PM" in str(secondTime):
        convertedSecond+=(12*60)


    converted = str(convertedFirst) + "-" + str(convertedSecond)
    return converted


testList = ['TuTh 10:30-11:45AM', 'MW 4-5:15PM', 'TuTh 8:30-9:45PM', 'TuTh 9-10:15AM', 'TuTh 12-1:15PM', 'MW 6-7:15PM', 'TuTh 6-6:50PM', 'TuTh 7-8:15PM', 'MW 1-1:50PM', 'MW 2-3:15PM', 'MW 10-11:15AM', 'M 7:30-8:20PM']

# Returns how long class is open for if it is available
# Else return false
def isOpen(classroomTimes):
    today = get_today()
    currentTime = get_current_time()
    for time in classroomTimes:
        if today in time[:-2]: #Strips AM/PM for monday
            startTime = convert_time(time).split('-')[0]
            endTime = convert_time(time).split('-')[1]
            if int(startTime) < currentTime < int(endTime):
                print("Class is used", time)
                return False
    # If none of the times are used by either day or time, it is open
    return True


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
