#Rhombus Star Pattern
"""
           ****
            ****
             ****
              ****
"""
n=4
for i in range(1,n+1):
    
    for j in range(1,n+1):
        print("*",end="")
    print()
    for k in range(1,i+1):
      print("",end=" ")
