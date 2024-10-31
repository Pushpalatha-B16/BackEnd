""" 2)Write a Python program to create a calculator class. Include methods for basic
arithmetic operations.( Addition, Subtraction, Multiplication,  Division )"""

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
c=Calculator(10,5)
print(c.addition())
print(c.subtraction())
print(c.multiplication())
print(c.division())
