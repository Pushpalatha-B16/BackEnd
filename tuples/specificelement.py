#Access and print the first and last element
n=int(input("number of items:"))
colors=tuple()
l=list(colors)
for i in range(n):
    i=input()
    l.append(i)
colors=tuple(l)
print("Access the element")
for i in colors:
    print(i)
print(f"First element:{colors[0]}")
print(f"Last element:{colors[-1]}")    
