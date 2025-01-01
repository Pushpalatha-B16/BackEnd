#Hollow Rectangle Star Pattern
"""
           ******
           *    *
           *    *
           ******
"""
l=int(input("enter value:"))
b=int(input("enter value:"))
for i in range(1,l+1):
    if i==1 or i==l:
        for j in range(1,b+1):
            print("*",end="")
        print()
    else:
        for j in range(1,b+1):
            if j==1 or j==b:
              print("*",end="")
            else:
                print("",end=" ")
        print()
