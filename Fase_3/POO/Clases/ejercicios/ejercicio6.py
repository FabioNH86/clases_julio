#Exercise 6: Class Inheritance
#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle 
#is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a 
#maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of 
#the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the
#fare() method of a Vehicle class in Bus class.

#Expected Output:
#Total Bus fare is: 5500.0

class Vehicle():
    def __init__(self,name,speed,mileage,seatingcapacity):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.seatingcapacity = seatingcapacity
        self.color = "white"
    def fare(self):
        finalfare = self.seatingcapacity *100
        return finalfare


class Bus(Vehicle):
    def busfare(self):
        finalfare = super().fare() + super().fare() * 0.1
        return finalfare
bus = Bus("bus",180,20,50)
vehicle = Vehicle("vehicle",250,20,6)
print(f"Total vehicle fare is {vehicle.fare()}")
print(f"Total bus fare is {bus.busfare()}")