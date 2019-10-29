from Database import *
from Time import *

class Location():
    def __init__(self, name):
        database = Database()
        time = Time()
        self.name = name
        self.times = database.get_times(self.name)
        #self.duration = time.mins_since_midnight
        self.duration = time.minutesLeft(self.times)
        self.status = self.duration > 0 # occupied or unoccupied


    def get_status(self):
        if self.status:
            return "UNOCCUPIED"
        else:
            return "VACANT"

    def get_duration(self):
        if self.duration > 1500:
            return "rest of day"
        elif self.duration > 0:
            return self.duration
        else:
            return - self.duration
