
#hollow pyramid pattern[final row=2*row-1 stars]

n=8
for i in range(1,n):
    for s in range(1,n-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        if j==1 :
            print("*",end=" ")
        elif j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
for k in range(1,n+1):
        print("*",end=" ")
"""

       * 
      * * 
     *   * 
    *     * 
   *       * 
  *         * 
 *           * 
* * * * * * * *"""

