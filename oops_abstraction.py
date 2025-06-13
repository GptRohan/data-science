from abc import ABC, abstractmethod

# base class for vehicles
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # every vehicle must have this method
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# car class implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} {self.model} car engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} car engine stopped.")

# bike class implementing abstract methods
class Bike(Vehicle):
    def start_engine(self):
        print(f"{self.brand} {self.model} bike engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} bike engine stopped.")

# create objects
my_car = Car("Toyota", "Fortuner")
my_bike = Bike("Yamaha", "R15")

# use methods
my_car.start_engine()
my_car.stop_engine()

my_bike.start_engine()
my_bike.stop_engine()
