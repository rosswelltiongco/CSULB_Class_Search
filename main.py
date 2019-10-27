

def getOpenClasses(building):
    sortedClassesAndTimes = []
    for classroom in allInfo:
        if building in classroom:
            appendList = [classroom, util.minutesLeft(allInfo[classroom])]
            sortedClassesAndTimes.append(appendList)

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


print("FIND OPEN ROOMS IN VEC & ECS SORTED BY DURATION\n")
# print("{} Unique runs since 4/15/2019".format(runCounter))
print("Day:",util.get_today())
time = util.get_current_time()
print("Time: {}: {}".format(time//60,time%60))
print("--------------------------------------")
printShit("VEC")
print("\n\n")
printShit("ECS")
