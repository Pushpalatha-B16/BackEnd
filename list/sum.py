#Write a Python program to sum all the items in a list
user=int(input("value:"))
a=[]
total=0
for i in range(1,user+1):
    i=int(input())
    a.append(i)
for j in range(0,len(a)):     
    total+=a[j]
print(f"sum of items in a list:{total}")    
    

   

    
