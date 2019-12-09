# SI 507, Fall 2019 - final project
# Developed by Gui Ruggiero

class Site():
    def __init__(self, name, country):
        self.created_by = 1
        
        self.name = name
        self.country = country

        self.lat = 0.0
        self.lgn = 0.0
        self.max_depth = 0.0
        self.notes = "notes"
        self.water = "water" # water environment type
        self.salinity = "salinity"

    def __str__(self):
        return self.name + " @ " + self.country

class Dive():
    def __init__(self, start_date, start_time, total_time, max_depth):
        self.diver = 1
        self.site = 0
        
        self.start_date = start_date
        self.start_time = start_time # how to format and attribute?
        self.total_time = total_time
        self.max_depth = max_depth
        
        self.start_pressure = 0
        self.end_pressure = 0
        self.surface_temp = 0
        self.bottom_temp = 0
        self.weights = 0
        self.dive_center = "dive_center"
        self.boat = "boat"
        self.structures = "structures"
        self.animals = "animals"
        self.rating = 0
        self.favorite = False
        self.photo_album = "photo_album"
        self.notes = "notes"
        self.validated = False
        self.gas = "gas"
        self.share_oxygen = 0.0
        self.share_nitrogen = 0.0
        self.share_helium = 0.0
        self.surface_supplied = False
        self.bottom_type = "bottom"
        self.transportation = "transportation"
        self.entry = "entry" # giant step, backroll, etc.
        self.drift = False
        self.night = False
        self.deep = False
        self.wreck = False
        self.cave = False
        self.ice = False
        self.altitude = False
        self.decompression = False
        self.rescue = False
        self.photo = False
        self.training = False
        self.buddy = "buddy"
        self.stop_depth = 0.0
        self.stop_duration = 0

    def __str__(self):
        return self.name