
#Add a new movie to the list and print the updated list
n=int(input("Number of movies"))
movies=[]
for i in range(n):
    i=input()
    movies.append(i)
print(f"list of movies:{movies}")    
new=input("Enter movie :")
movies.append(new)
print(f"updated movie list:{movies}")
