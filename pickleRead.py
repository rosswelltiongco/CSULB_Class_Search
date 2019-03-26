

import pickle
import utilities as util

f = open('store.pckl', 'rb')
allInfo = pickle.load(f)
f.close()

print(allInfo)

for classroom in allInfo:
        print(classroom,util.isOpen(allInfo[classroom]))
