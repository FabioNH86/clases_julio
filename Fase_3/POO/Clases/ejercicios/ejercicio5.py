    #Exercise 5: Define a property that must have the same value for every class instance (object)
#Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
#Add an empty 'Bus' and 'Car' SubClasses of the 'Vehicle' Class.

#Expected Output:
#Color: White Vehicle name: School Volvo Speed: 180 Mileage: 12
#Color: White Vehicle name: Audi Q5 Speed: 240 Mileage: 18
class Vehicle():
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.color = "white"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
    

bus = Bus("School Volvo",180,12)
car = Car("Audi Q5",240,18)

print(f"Color: {bus.color}, Name: {bus.name}, Speed: {bus.speed}, mileage: {bus.mileage}")
print(f"Color: {car.color}, Name: {car.name}, Speed: {car.speed}, mileage: {car.mileage}")
