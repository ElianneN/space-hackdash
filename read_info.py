# Hackdash_MergeVerse
import planets
while True:
    print("Option 1: lists of planets\nOption 2: compare by size\nOption 3: filter\nOption 4: exit")

    choice = input("please select one of the options: ")
    if choice == "1":
        read_planet = []
        with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
            for line in file:
                read_planet.append(line.strip())
  
        for planet in read_planet:
            planets.name, planets.size, planets.distance_from_sun, planets.moons, planets.description = planet.split(",")
            print("Name:", planets.name)
            print("Size:", planets.size)
            print("Distance from Sun:", planets.distance_from_sun)
            print("Moons:", planets.moons)
            print()

    elif choice == "2":
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

    elif choice == "3":
        #terminal menu option 3: filter attribute outputted based on user input, always include name in the output with the selected attribute
        #allow user to enter return to main menu or exit after displaying filtered results

        attribute = input("Enter the attribute to filter by (size, distance_from_sun, moons, description) or press any key to return to main menu: ").strip().lower()
        valid_attributes = {"size", "distance_from_sun", "moons", "description"}

        if attribute not in valid_attributes:
            main_menu = input("Return to main menu? (yes/no): ").strip().lower()
            if main_menu != "yes":
                choice()
            elif main_menu == "no":
                attribute = input("Enter the attribute to filter by (size, distance_from_sun, moons, description) or press any key to return to main menu: ").strip().lower()

        read_planet = []
        with open('textfiles/planets.txt', "r", encoding="utf-8") as file:
            next(file)  # Skip header line
            for line in file:
                read_planet.append(line.strip())

        for planet in read_planet:
            name, size, distance_from_sun, moons, description = planet.split(",")
            planet_obj = planets.planets(name, size, distance_from_sun, moons, description)
        
        if attribute == "size":
            print("Size:", planet_obj.size)
        elif attribute == "distance_from_sun":
            print("Distance from Sun:", planet_obj.distance_from_sun)
        elif attribute == "moons":
            print("Moons:", planet_obj.moons)
        elif attribute == "description":
            print("Description:", planet_obj.description)
            
    elif choice == "4":
        break
    else:
        print("Invalid choice. please choose 1, 2,or 3")



