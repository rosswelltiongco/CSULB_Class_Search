from Database import *
from Time import *
from Location import *

class Building:
    def __init__(self, building_name):
        database = Database()
        self.name = building_name
        self.locations = [Location(x) for x in database.get_locations() if self.name in x]
        self.locations.sort(key=lambda location: location.duration, reverse=True)


    def get_open_classes(self):
        for location in self.locations:
            print(location.name, location.status)


building = Building("VEC")

for location in building.locations:
    print(location.name, location.get_status(), location.get_duration())



"""
def getOpenClasses(self, building):
    sortedClassesAndTimes = []
    iterate = 0
    locations = self.database.get_locations()

    for classroom in locations:
        if building in classroom:
            appendList = [classroom, self.time.minutesLeft(self.database.get_times(locations[iterate]))]
            #appendList = [classroom, self.time.minutesLeft(locations[iterate])] # GREAT EXAMPLE FOR DEBUGGING
            sortedClassesAndTimes.append(appendList)
        iterate += 1

    sortedClassesAndTimes.sort(key=lambda x: x[1], reverse=True)
    return sortedClassesAndTimes


def printShit(self, building):
    for room in self.getOpenClasses(building):
        if(room[1] > 1500): # was 1500 #FIXME: Change to total mins in day - current mins (i.e remaining mins of day)
            print(room[0],"VACANT for rest of day")
        elif (room[1]) > 0:
            print("{} VACANT for {} hrs and {} mins".format(room[0], room[1] // 60, room[1] % 60))
        else:
            print("{} OCCUPIED for {} hrs and {} mins".format(room[0], -room[1] // 60, -room[1] % 60))
"""