
#Write a Python program to get the largest number from a list.
user=int(input("number of items:"))
a=[]
for i in range(user):
    i=int(input())
    a.append(i)
print(f"largest number:{max(a)}")

#without using max 
user=int(input("number of items:"))
a=[]
#maximum=0
for i in range(user):
    i=int(input())
    a.append(i)
maximum=a[0]    
for j in a:
    if j>maximum:
        maximum=j
print(f"largest number:{maximum}")


