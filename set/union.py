#create a another set of fruits and find the union and intersection of both sets
def fun():
      n=int(input("Number of items:"))
      s=set() 
      for i in range(n):
       i=input()
       s.add(i)
      return s
s1=fun()
print(s1)
s2=fun()
print(s2)
print(f"union:{s1.union(s2)}")
print(f"intersection:{s1.intersection(s2)}")
