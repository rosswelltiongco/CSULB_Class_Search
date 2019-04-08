

import json
import utilities as util


with open('data.json') as json_file:
    allInfo = json.load(json_file)

"""
# good to test for all classes/building/floor
for classroom in allInfo:
    if "ECS-4" in classroom:
        print(classroom,util.minutesLeft(allInfo[classroom]))
"""

def getOpenClasses(building):
    sortedClassesAndTimes = []
    for classroom in allInfo:
        if building in classroom:
            appendList = [classroom, util.minutesLeft(allInfo[classroom])]
            sortedClassesAndTimes.append(appendList)

    sortedClassesAndTimes.sort(key = lambda x: x[1], reverse=True)
    return sortedClassesAndTimes


[print(room) for room in getOpenClasses("ECS")]
