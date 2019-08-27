 # Parse class schedule


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

roomTimes = {} # Stores classes and the times they are occupied
allClasses = []


"""GETTING DEPT URLS"""
all_subjects_url = "http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2019/By_Subject/"

uClient = uReq(all_subjects_url)

with uReq(all_subjects_url) as something:
    page_html = something.read()
# Parse HTML
page_soup = soup(page_html, "html.parser")
containers = page_soup.find("div",{"class":"indexList"})

# Get all href links
links = [link.get('href') for link in containers.findAll('a')]
links = [x for x in links if x is not None]


subject_urls = []
for subject in links:
  if '.html' in subject:
    subject_urls.append(all_subjects_url+subject)
  else:
    pass


"""PARSING A SINGLE CLASS"""
def parse_subject(subject_url):
    print("PARSING:",subject_url)
    uClient = uReq(subject_url)

    page_html = uClient.read()
    uClient.close()

    # Parse html
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"courseBlock"})

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

                # Storing rooms and the times they are occupied
                # into separate dictionary
                if room not in roomTimes:
                    roomTimes[room] = [day + " " + time]
                else:
                    #just update
                    roomTimes[room].append(day + " " + time)

                tempClassInfo = [id,className,day,time,room,prof]
                allClasses.append(tempClassInfo)

def getRooms():
    [parse_subject(url) for url in subject_urls]
    return allClasses
