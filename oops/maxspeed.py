"""6)Create a Vehicle class with max_speed and year instance attributes"""

class Vehicle:
    def __init__(self,max_speed,year):
        self.m=max_speed
        self.y=year
    def display(self):
        print(f"max_speed:{self.m}")
        print(f"year:{self.y} ")
v=Vehicle(50,2000)
v.display()



