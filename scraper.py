from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

rooms = {}

#Setup
my_url = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2018/By_Subject/CECS.html"
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"courseBlock"})

"""
firstCourse = containers[0]
className = firstCourse.h4.text

sections = firstCourse.findAll("tr")

firstSection = sections[4]
if firstSection.th.text == "SEC.":
    print("skip me")
    #break
else:
    data = [x.text for x in firstSection.findAll("td")]

    day = data[5]
    time = data[6]
    room = data[8]
    prof = data[9]

    print(day,time,room,prof)
"""

for container in containers:
    className = container.h4.text
    sections = container.findAll("tr")
    for section in sections:
        if section.th.text=="SEC.":
            # break
            pass
        else:
            data = [x.text for x in section.findAll("td")]

            day = data[5]
            time = data[6]
            room = data[8]
            prof = data[9]

            if room not in rooms:
                rooms[room] = [day+time]
            else:
                #just update
                rooms[room].append(day+time)


print(rooms["ECS-404"])
print(len(rooms["ECS-404"]))
