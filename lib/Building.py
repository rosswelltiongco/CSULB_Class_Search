class Search():
    # Should I make a search class?
    pass

from Database import *
from Time import *
from Location import *

class Building:
    def __init__(self, building_name):
        database = Database()
        self.name = building_name
        self.locations = [Location(x) for x in database.get_locations() if self.name in x]
        self.locations.sort(key=lambda location: location.get_duration(), reverse=True)
        # TODO: for unoccupieds: sort by longest duration

    def get_open_classes(self):
        for location in self.locations:
            print(location.name, location.status)

    def set_time(self, hour, minutes, ampm):
        mins_since_midnight = (hour + 12*(ampm.upper() == "PM")) * 60 + minutes
        
        for location in self.locations:
            location.set_time(mins_since_midnight)


    def set_day(self, day):
        for location in self.locations:
            location.set_day(day)

building = Building("VEC")


#"""
# To change time
building.set_time(9,30,'pm')
#"""

for location in building.locations:
    #print(location.name, location.duration)
    print(location.name, location.get_status(), location.get_duration(), location.time.get_time())


#vec321 = database.get_times("VEC-321")
#print(vec321)

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