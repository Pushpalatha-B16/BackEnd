"""
Swapping Variable Values Without an Intermediary Variable

Problem: You have two variables, a and b, and you want to swap their values
without using an intermediary variable. This operation is commonly referred
to as a "value swap." """

a=int(input("value1:"))
b=int(input("value2:"))
print(f"before swap:{a,b}")
a,b=b,a
print(f"After swap:{a,b}")
