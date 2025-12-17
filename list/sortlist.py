#sort the  list of movies in alphabetical order and print it
n=int(input("Number of movies:"))
movies=[]
for i in range(n):
    i=input()
    movies.append(i)
print(f"Movies:{movies}")
movies.sort()
print(f"sorted the list:{movies}")
