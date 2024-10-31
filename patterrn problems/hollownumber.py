n=8
for i in range(1,n):
    for s in range(1,n-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        if j==1 :
            print(j,end=" ")
        elif j==i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()  
for k in range(1,n+1):
        print(k,end=" ")

"""        
       1 
      1 2 
     1   3 
    1     4 
   1       5 
  1         6 
 1           7 
1 2 3 4 5 6 7 8 """
