#reverse hollow using half pyramid
"""
* * * * 
*   * 
*  * 
* * 
* 
"""
n=5
for k in range(1,n):
    print("*",end=" ")
print()
for j in range(n-1,0,-1):
 for i in range(1,j+1):
    if i==1:
        print("*",end=" ")
    elif i==j:
        print("*",end=" ")
    else:
        print("",end=" ")
 print()
