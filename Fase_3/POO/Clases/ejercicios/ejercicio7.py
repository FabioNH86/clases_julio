#Exercise 7: Check type of an object
#Write a program to determine which class a given Bus object belongs to.

#Given:
class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

busprime = Bus(180,12)
print(type(busprime))
print(type(KeyError))
print(type(Bus))
a = 4
print(type(a))
print(type(int))

a2 = "huosdfjo_"
a3 = "jioioifg"
print(a2 + a3)