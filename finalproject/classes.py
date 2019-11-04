# SI 507 - final project, classes
# Developed by Gui Ruggiero

class DiveSite():
    def __init__(self, name, lat, lgn):
        self.name = name
        self.lat = lat
        self.lgn = lgn

    def __str__(self):
        return self.name

class Dive():
    def __init__(self, name, date, time, duration, max_depth):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.max_depth = max_depth

    def __str__(self):
        return self.name