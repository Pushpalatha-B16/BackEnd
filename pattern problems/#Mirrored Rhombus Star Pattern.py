#Mirrored Rhombus Star Pattern
"""
           ****
          ****
         ****
        ****
"""
n=4
for i in range(n):
    for k in range(n,i-1,-1):
        print("",end=" ")
    for j in range(n):
        print("*",end="")
    print()
