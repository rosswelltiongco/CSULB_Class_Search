from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
rooms = {}
roomList = []

"""GETTING DEPT URLS"""
my_url = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/index.html"
uClient = uReq(my_url)

with uReq(my_url) as something:
    page_html = something.read()
#html parsing
page_soup = soup(page_html, "html.parser")

starterLink="http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2019/By_Subject/"
containers = page_soup.find("div",{"class":"indexList"})
# for link in containers.findAll('a'):
#     print(link.get('href'))

links = [link.get('href') for link in containers.findAll('a')]
links = [x for x in links if x is not None]


goodUrls = []
for item in links:
  if '.html' in item:
    goodUrls.append(starterLink+item)
  else:
    pass



"""GETTING FROM SINGLE CLASS"""
#Setup
def doMajor(url):
    print("DOING:",url)
    my_url = url
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
                id = data[0]
                className = className[:8]
                className = className.replace('-','')
                className = className.rstrip()
                day = data[5]
                time = data[6]
                room = data[8]
                prof = data[9]

                if room not in rooms:
                    rooms[room] = [day+time]
                else:
                    #just update
                    rooms[room].append(day+time)
                tempList = [id,className,day,time,room,prof]
                roomList.append(tempList)

def getRooms():
    # for item in goodUrls:
        # doMajor(item)
    [doMajor(url) for url in goodUrls]
    return roomList
