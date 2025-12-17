#pyramid pattern with alphabet
"""
    A 
   A B 
  A B C 
 A B C D 
A B C D E """


n=5
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print("",end=" ")
    a=65
    for j in range(1,i+1):
        c=chr(a)
        print(c,end=" ")
        a+=1
    print()
