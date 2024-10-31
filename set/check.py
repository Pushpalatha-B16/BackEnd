#check if speific fruits in set
n=int(input("Number of items:"))
s=set()
for i in range(n):
    i=input()
    s.add(i)
print(f"Favourite fruits:{s}")
n=input("enter fruit")
print(f"check a fruit in the set or not:{n in s}")
