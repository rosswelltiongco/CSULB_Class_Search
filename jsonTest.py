import json

r = {'is_claimed': 'True', 'rating': 3.5}

with open('data.json', 'w') as outfile:
    json.dump(r, outfile)


with open('data.json') as json_file:
    r = json.load(json_file)
    print(r)
