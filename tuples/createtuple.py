#create tuple with your favourite  colors and print it
n=int(input("number of items:"))
colors=tuple()
l=list(colors)
for i in range(n):
    i=input()
    l.append(i)
colors=tuple(l)
print(f"Favourite colors:{colors}")
    
