#Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Porsche(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)


class Tsuru(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
    
porsche = Porsche(330,0)
tsuru = Tsuru(100,100000)
print(f"El porsche alcanza una velocidad de:{porsche.max_speed} y tiene {porsche.mileage} millas recorridas")
print(f"El tsuru alcanza una velocidad de:{tsuru.max_speed} y tiene {tsuru.mileage} millas recorridas")