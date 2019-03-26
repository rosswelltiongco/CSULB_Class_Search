

import pickle

test = {'1':[1,2,3],"2":[2,3,4],"3":[5,6,7]}


f = open('store.pckl', 'wb')
pickle.dump(test, f)
f.close()

f = open('store.pckl', 'rb')
test = pickle.load(f)
print(test)
f.close()
