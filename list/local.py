"""Write a sample program for Local Variable and Global Variable
Describe how they differ,"""
a=5
b=8
def fun():
    a=6
    return a+b
print(f"sum of a:{a},b:{b},a+b:{fun()}")
print(f"sum of a:{a},b:{b},a+b:{a+b}")
