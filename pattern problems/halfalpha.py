#half pyramid pattern in alphabets
"""
A 
B B 
C C C 
D D D D """

n=int(input())
a=65
for i in range(1,n+1):
    for j in range(1,i+1):
        c=chr(a)
        print(c,end=" ")
    a+=1
    print()

