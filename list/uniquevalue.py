"""Finding unique values in a list  You have a list 1st containing several values, and you want to extract only the
unique values from the list.
sample input: lst = [ 1,2,3,4,4,6,7,7,3,5,2,7]
sample output : [1, 2, 3, 4, 5, 6, 7]
The output will be a list of the uniq ue values from the original list, without any
duplicates"""
a=[]
n=int(input("number of element:"))
for i in range(1,n+1):
    i=int(input())
    a.append(i)
print(f"original values:",a)
unique=set(a)
unique=list(unique)
print(f"unique values:{unique}")
