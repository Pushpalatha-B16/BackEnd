#inverted full pyramid pattern
"""
***************
 *************
  ***********
   *********
    *******
     *****
      ***
       *
"""
n=int(input())
for i in range(n,0,-1):
    for s in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
