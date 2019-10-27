from lib.Database import *
from lib.Time import *


database = Database()

time = Time()


locations = database.get_locations()


#"""
def getOpenClasses(building):
    sortedClassesAndTimes = []
    iterate = 0
    for classroom in locations:
        if building in classroom:
            appendList = [classroom, time.minutesLeft(locations[iterate])]
            sortedClassesAndTimes.append(appendList)
        iterate += 1

    sortedClassesAndTimes.sort(key=lambda x: x[1], reverse=True)
    return sortedClassesAndTimes


def printShit(building):
    for room in getOpenClasses(building):
        if(room[1] > 1500): # was 1500 #FIXME: Change to total mins in day - current mins (i.e remaining mins of day)
          print(room[0],"VACANT for rest of day")
        elif (room[1]) > 0:
            print("{} VACANT for {} hrs and {} mins".format(
                room[0], room[1] // 60, room[1] % 60))
        else:
            print("{} OCCUPIED for {} hrs and {} mins".format(
                room[0], -room[1] // 60, -room[1] % 60))


printShit("VEC")
#"""

