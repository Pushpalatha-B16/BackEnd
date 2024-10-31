#count the number of movies
n=int(input())
movies=[]
for i in range(n):
    i=input()
    movies.append(i)

print(f"movies:{movies}")
print(f"Number of movies:{len(movies)}")
