#create a set of your favourite fruits and print it
n=int(input("Number of items:"))
s=set()
for i in range(n):
    i=input()
    s.add(i)
print(f"Favourite fruits:{s}")
#Remove a fruit from the set and print updated set
remove=input("enter remove fruit")
s.discard(remove)
print(f"Updated set:{s}")
