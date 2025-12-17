#pyramid pattern with number
"""
    1
   123
  12345
 1234567
123456789"""

n=5
for i in range(1,n+1):
   for j in range(1,n-i+1):
       print(" ",end="")
   for k in range(1,2*i):#it is imporatant
       print(k,end="")
   print()
