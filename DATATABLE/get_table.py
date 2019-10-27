import scrape_classes as scrape
import json
all_sections = scrape.getRooms()

f = open("html_table.txt", "w")

html_text = ""
json_text = ""
json_all = []
for section in all_sections:
    if "E E" in section[1]:
        row_text = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>".format(section[0],section[1],section[2],section[3],section[4],section[5])
        html_text += row_text

    # <tr>
    #   <td>Tatyana Fitzpatrick</td>
    #   <td>Regional Director</td>
    #   <td>London</td>
    #   <td>19</td>
    #   <td>2010/03/17</td>
    #   <td>$385,750</td>
    # </tr>


    # a Python object (dict):
    json_data = {}
    json_data["Section"] = section[0]
    json_data["Class"] = section[1]
    json_data["Day"] = section[2]
    json_data["Time"] = section[3]
    json_data["Room"] = section[4]
    json_data["Professor"] = section[5]
    json_all.append(json_data)
    # convert into JSON:


    # the result is a JSON string:
    
    # {
    #   "company": "OVERPLEX",
    #   "place": "EUA",
    #   "name": "Cannon Morin"
    # },

f.write(html_text)
f.close()

with open('json.txt', 'w') as outfile:
    json.dump(json_all, outfile)