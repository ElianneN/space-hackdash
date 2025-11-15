#reading info from planets.txt, storing the objects in array
##import pandas as pd
##df = pd.read_csv("C:\\Users\\molly\\space-hackdash\\textfiles\\planets.txt")
##df.head()
#with open closes the text file after reading it
with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
class planets:
    def __init__(self, name, size, distance_from_sun, moons):
        self.name = name
        self.size = size
        self.distance_from_sun = 0
        self.moons = moons
        planet_data =[name, size, distance_from_sun, moons]
        self.componets = []
    def add_componets(self, componet):
        self.componets.append(componet)
    print(planets.__init___())
    
