from Database import *
from Time import *

class Location():
    def __init__(self, name):
        self.database = Database()
        self.time = Time()

        self.name = name
        self.times = self.database.get_times(self.name)
        #self.duration = time.mins_since_midnight
        #self.duration = self.time.minutesLeft(self.times)
        #self.status = self.duration > 0 # occupied or unoccupied


    def get_status(self):
        if self.time.minutesLeft(self.times) > 0:
            return "UNOCCUPIED"
        else:
            return "OCCUPIED"
        """
        if str(self.get_duration()) == "rest of day":
            return "UNOCCUPIED"
        elif (self.get_duration() > 0):
            return "UNOCCUPIED"
        else:
            return "OCCUPIED"
        """

    def get_duration(self):
        duration = self.time.minutesLeft(self.times)
        if duration > 1500:
            return "rest of day"
        elif duration > 0:
            return duration
        else:
            return - duration

    def set_day(self, day):
        self.time.set_day(day)
    
    def set_time(self, time):
        self.time.set_time(time)

