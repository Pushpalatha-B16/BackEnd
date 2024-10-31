"""Given a list 1st with elements [2, 33,222, 14, 25], youwant to subtract 1from each element in the list.
sample input :  [2, 33, 222, 14, 25]
sample output : [l, 32,221, 13, 24]
(The code creates a new list called result where each
element in 1st is reduced by 1)"""
l= [2, 33, 222, 14, 25]
result=[]
print("old list:",l)
for i in l:
    a=i-1
    result.append(a)
print(f"new list:{result}")
















