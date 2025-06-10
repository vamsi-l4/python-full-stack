class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("Beep beep!")

# Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent class constructor
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Creating an object of the child class
my_car = Car("Honda", "Civic")
my_car.display_info()  # Output: Honda Civic
my_car.honk()          # Output: Beep beep!
