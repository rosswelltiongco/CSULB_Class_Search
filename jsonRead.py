

import json
import utilities as util


with open('data.json') as json_file:
    allInfo = json.load(json_file)
    # print(allInfo)


for classroom in allInfo:
        print(classroom,util.isOpen(allInfo[classroom]))
