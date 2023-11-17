class TransportCompany:
    def __init__(self):
        self.cities = []
        self.drivers = {}

    def add_city(self, city):
        self.cities.append(city)

    def add_driver(self, driver_name, route):
        self.drivers[driver_name] = route

    def add_city_to_driver_route(self, driver_name, city_name, position):
        if driver_name in self.drivers and city_name in self.cities:
            route = self.drivers[driver_name]
            if position == 1:
                route.insert(0, city_name)
            elif position == -1:
                route.append(city_name)
            elif 0 < position <= len(route):
                route.insert(position - 1, city_name)
            else:
                print("Invalid position.")
        else:
            print("Driver or city not found.")

    def remove_city_from_driver_route(self, driver_name, city_name):
        if driver_name in self.drivers:
            route = self.drivers[driver_name]
            if city_name in route:
                route.remove(city_name)
            else:
                print(f"{city_name} not found in the route of {driver_name}.")
        else:
            print("Driver not found.")

    def check_deliverability(self, target_city):
        eligible_drivers = [driver for driver, route in self.drivers.items() if target_city in route]
        if eligible_drivers:
            print(f"Drivers who deliver to {target_city}: {', '.join(eligible_drivers)}")
        else:
            print(f"No drivers deliver to {target_city}.")

# Example usage
transport_system = TransportCompany()

while True:
    print("\nOptions:")
    print("1. Add a city")
    print("2. Add a driver")
    print("3. Add a city to the route of a driver")
    print("4. Remove a city from a driver's route")
    print("5. Check the deliverability of a package")

    choice = input("Enter your choice (1-5, or 'exit' to end): ")

    if choice == '1':
        city_name = input("Enter the name of the city: ")
        transport_system.add_city(city_name)
        print(f"City '{city_name}' added successfully.")

    elif choice == '2':
        driver_name = input("Enter the name of the driver: ")
        route = input("Enter the route of the driver (comma-separated cities): ").split(',')
        transport_system.add_driver(driver_name, route)
        print(f"Driver '{driver_name}' added successfully with route {route}.")

    elif choice == '3':
        driver_name = input("Enter the name of the driver: ")
        city_name = input("Enter the name of the city to add: ")
        position = int(input("Enter the position to add the city (1 for the beginning, -1 for the end, or index): "))
        transport_system.add_city_to_driver_route(driver_name, city_name, position)

    elif choice == '4':
        driver_name = input("Enter the name of the driver: ")
        city_name = input("Enter the name of the city to remove: ")
        transport_system.remove_city_from_driver_route(driver_name, city_name)

    elif choice == '5':
        target_city = input("Enter the name of the city for package delivery: ")
        transport_system.check_deliverability(target_city)

    elif choice.lower() == 'exit':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
