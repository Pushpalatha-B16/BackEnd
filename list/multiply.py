#Write a Python program to multiply all the items in a list.
user=int(input("number of items:"))
a=[]
m=1
for i in range(user):
    i=int(input())
    a.append(i)
for j in range(0,len(a)):
    m*=a[j]
print(f"Multiplication of all items in a list:{m}") 
