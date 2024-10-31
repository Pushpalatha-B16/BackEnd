"""3)Create a child class Bus that will inherit all of the variables and methods
of the Vehicle class(Parent class)"""
class Vehicle:
    def __init__(self,name,price):
        self.vechicle_n=name
        self.p=price
    def display(self):
        print(f"name:{self.vechicle_n}")
        print(f"price:{self.p}")
class Bus(Vehicle):
    def __init__(self,name,price):
        super().__init__(name,price)
    def display(self):
        super().display()
b=Bus("Bus",10000)
b.display()

