#Remove the first movie from the list and print the updated list
n=int(input("Number of movies"))
movies=[]
for i in range(n):
    i=input()
    movies.append(i)
print(f"list of movies:{movies}")    
removed=input("removed movie name:")
r=movies.index(removed)
movies.pop(r)
print(f"updated list:{movies}")
