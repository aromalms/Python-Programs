#hierarchical inheritance
class Vehicle:
 def info(self):
    print("This is Vehicle")
class Car(Vehicle):
 def car_info(self, name):
    print("Car name is:", name)
class Truck(Vehicle):
 def truck_info(self, name):
    print("Truck name is:", name)
class Bike(Vehicle):
    def bike_info(self, name):
        print("Bike name is:", name)
car = Car()
car.info()
car.car_info('BMW')
truck = Truck()
truck.info()
truck.truck_info('Tata')
bike=Bike()
bike.info()
bike.bike_info('Honda')