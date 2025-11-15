#terminal menu option 2: compare by size
import planets
def compare_size():
    read_planet = []
    with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
        next(file)  # Skip header line
        for line in file:
            read_planet.append(line.strip())

    planet_objects = []
    for planet in read_planet:
        name, size, distance_from_sun, moons, description = planet.split(",")
        planet_obj = planets.planets(name, size, distance_from_sun, moons, description)
        planet_objects.append(planet_obj)

    size_order = {"Small": 1, "Medium": 2, "Large": 3}
    planet_objects.sort(key=lambda x: size_order.get(x.size, 0))

    for planet in planet_objects:
        print("Name:", planet.name)
        print("Size:", planet.size)
        print("Distance from Sun:", planet.distance_from_sun)
        print("Moons:", planet.moons)
        print("Description:", planet.description)
        print()

#terminal menu option 3: filter attribute outputted based on user input, always include name in the output with the selected attribute
def filter_attribute():
    attribute = input("Enter the attribute to filter by (size, distance_from_sun, moons, description): ").strip().lower()
    valid_attributes = {"size", "distance_from_sun", "moons", "description"}

    if attribute not in valid_attributes:
        print("Invalid attribute. Please choose from size, distance_from_sun, moons, description.")
        return

    read_planet = []
    with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
        next(file)  # Skip header line
        for line in file:
            read_planet.append(line.strip())

    for planet in read_planet:
        name, size, distance_from_sun, moons, description = planet.split(",")
        planet_obj = planets.planets(name, size, distance_from_sun, moons, description)

        print("Name:", planet_obj.name)
        if attribute == "size":
            print("Size:", planet_obj.size)
        elif attribute == "distance_from_sun":
            print("Distance from Sun:", planet_obj.distance_from_sun)
        elif attribute == "moons":
            print("Moons:", planet_obj.moons)
        elif attribute == "description":
            print("Description:", planet_obj.description)