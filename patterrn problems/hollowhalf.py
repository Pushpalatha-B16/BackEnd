#hollow half pyramid in python
"""
* 
* * 
*   * 
*     * 
* * * * * 
"""

n=5
for i in range(1,n):
    for j in range(1,i+1):
        if j==1:
          print("*",end=" ")
        elif j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for k in range(1,n+1):
      print("*",end=" ")

