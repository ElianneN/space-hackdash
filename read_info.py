#reading info from planets.txt, storing the objects in array
#with open closes the text file after reading it
import planets

read_planet = []
with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
    for line in file:
        read_planet.append(line.strip())

print(read_planet[0])   
for planet in read_planet:
    print(planet)
    planets.name, planets.size, planets.distance_from_sun, planets.moons, planets.description = planet.split(",")
    print("Name:", planets.name)
    print("Size:", planets.size)
    print("Distance from Sun:", planets.distance_from_sun)
    print("Moons:", planets.moons)
    print()
    
