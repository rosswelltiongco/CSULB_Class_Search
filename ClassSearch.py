from lib.Database import *
from lib.Time import *

class ClassSearch:
    def __init__(self):
        self.database = Database()
        self.time = Time()
        self.locations = self.database.get_locations()
        print("IT IS CURRENTLY: {}\nDAY: {}".format(self.time.get_time(), self.time.get_day()))

    def getOpenClasses(self, building):
        sortedClassesAndTimes = []
        iterate = 0
        for classroom in self.locations:
            if building in classroom:
                appendList = [classroom, self.time.minutesLeft(self.database.get_times(self.locations[iterate]))]
                #appendList = [classroom, self.time.minutesLeft(self.locations[iterate])] # GREAT EXAMPLE FOR DEBUGGING
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

class_search = ClassSearch()

class_search.printShit("ECS")


