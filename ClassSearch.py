from lib.Database import *
from lib.Time import *

class ClassSearch:
    def __init__(self):
        self.database = Database()
        self.time = Time()
        #print("IT IS CURRENTLY: {}\nDAY: {}".format(self.time.get_time(), self.time.get_day()))
