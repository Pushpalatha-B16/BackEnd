"""4)Create a Bus class that inherits from the Vehicle class. Give the capacity argument of
Bus.seating_capacity() a default value of 50."""

class Vehicle:
   pass
class Bus(Vehicle):
    
    def seating_capacity(self,capacity=50):
        print(f"seating_capacity:{capacity}")
b=Bus()
b.seating_capacity()
b.seating_capacity(100)


"""5)Create a Zoosystem class without any variables
 and methods"""
class Zoosystem :
    pass
