#Exercise 4: Class Inheritance
#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of 
#Bus.seating_capacity() a default value of 50.

#Expected Output:
#The seating capacity of a bus is 50 passengers

#Given:
class Vehicle():
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, speed, mileage,):
        super().__init__(name, speed, mileage)
    def seating_capacity(capacity):
        print(f"The seating capacity of a bus is {capacity} passengers")

bus = Vehicle.seating_capacity(50)