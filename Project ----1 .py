# Demonstration of Polymorphism in Python

class BMW:
    def fuel_type(self):
        print("BMW uses Petrol.")

    def max_speed(self):
        print("Maximum speed of BMW is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Diesel.")

    def max_speed(self):
        print("Maximum speed of Ferrari is 300 km/h.")

# Polymorphism implementation
def car_details(car):
    car.fuel_type()
    car.max_speed()

# Creating objects
