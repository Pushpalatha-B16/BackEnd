#Parallelogram Star Pattern
"""

           ******
            ******
             ******
              ******

"""
l=int(input("enter value:"))
b=int(input("enter value:"))
for i in range(1,l+1):
    for j in range(1,b+1):
        print("*",end="")
    print()
    for k in range(1,i+1):
        print("",end=" ")
