#reading info from planets.txt, storing the objects in array
#with open closes the text file after reading it
import planets
print("Option 1: lists of planets\nOption 2: compare by size\nOption 3: filter ")

choice = input("please select one of the options: ")
if choice == "1":
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

elif choice == "2":
    print()
elif choice == "3":
    print()
else:
    print("Invalid choice. please choose 1, 2,or 3")


