class planets:
    def __init__(self, name, size, distance_from_sun, moons, description):
        self.name = name
        self.size = size
        self.distance_from_sun = distance_from_sun
        self.moons = moons
        self.description = description
        planet_data =[name, size, distance_from_sun, moons]
        self.componets = []
    def add_componets(self, componet):
        self.componets.append(componet)