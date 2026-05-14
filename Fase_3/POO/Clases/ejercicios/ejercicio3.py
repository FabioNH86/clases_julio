#Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle 
#class

#Expected Output:
#Vehicle Name: School Volvo Speed: 180 Mileage: 12

#Given: 
class Vehicle():
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        
class Bus(Vehicle):
    def __init__(self, name, speed, mileage):
        super().__init__(name, speed, mileage)

bus = Bus("School Volvo",180,12)
print(f"Vehicle name: {bus.name},Speed: {bus.speed}, Mileage: {bus.mileage}")