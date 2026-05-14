#Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

buschido = Bus(180,10)
print(isinstance(buschido,Vehicle))
