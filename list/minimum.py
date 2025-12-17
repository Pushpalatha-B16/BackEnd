#Write a Python program to get the smallest number from a list.

user=int(input("number of items:"))
a=[]
for i in range(user):
    i=int(input())
    a.append(i)
print(f"smallest number:{min(a)}")
#without using mix
user=int(input("number of items:"))
a=[]
for i in range(user):
    i=int(input())
    a.append(i)
minimum=a[0]    
for j in a:
    if j<minimum:
        minimum=j
print(f"smallest number:{minimum}")
