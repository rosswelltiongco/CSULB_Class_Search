from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class Scraper:

    def __init__(self):
        self.full_schedule =  []


    def get_full_schedule(self):
        return self.full_schedule


    def get_soup_html(self, url):
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html,"html.parser")

        return page_soup


    def scrape_semester(self, semester_url):
        for subject_url in self.get_subject_urls(semester_url):
            self.scrape_subject(subject_url)


    def get_subject_urls(self, semester_url):
        html = self.get_soup_html(semester_url)
        containers = html.find("div", {"class":"indexList"})

        links = [link.get('href') for link in containers.findAll('a')]
        links = [x for x in links if x is not None]

        subject_urls = []
        for subject in links:
            if '.html' in subject:
                subject_urls.append(semester_url + subject)
        
        return subject_urls

    def scrape_subject(self, subject_url):
        print("Scraping:", subject_url)
        
        courses = self.get_soup_html(subject_url).findAll("div",{"class":"courseBlock"})

        for course in courses:
            self.scrape_course(course)


    def scrape_course(self, course):
        course_name = self.format_course_name(course.h4.text)

        sections = course.findAll("tr")

        for section in sections:
            if not self.is_header_row(section):
                data = [x.text for x in section.findAll("td")]

                class_number = data[0]
                days         = data[5]
                time         = data[6]
                location     = data[8]
                instructor   = data[9]

                course_info  = [class_number, course_name, days, time, location, instructor]
                self.full_schedule.append(course_info)


    def format_course_name(self, course_name):
        return course_name[:8].replace('-','').rstrip()


    def is_header_row(self, row):
        return row.th.text == "SEC."




