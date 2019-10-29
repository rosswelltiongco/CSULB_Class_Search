"""
Scrape and generate database
"""
from lib.Database import *
from lib.Scraper import *
import time


def main():

    start_time = time.time()
    scraper = Scraper()
    scraper.scrape_semester("http://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2019/By_Subject/")

    full_schedule = scraper.get_full_schedule()
    database = Database()
    database.make_database(full_schedule)
    end_time = time.time()

    total_time = end_time - start_time

    print("Took {} seconds to scrape and insert {} items".format(total_time[:5], len(full_schedule)))

main()