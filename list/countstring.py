"""
Write a Python program to count the number of strings from a given
list of strings. The string length is 2 or more and the
first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """
user=int(input("number of items:"))
a=[]

for i in range(user):
    i=input()
    a.append(i)
if len(a)>=2:
      c=0
      for j in range(1,len(a)-1):
          c+=1
      print(f"The length of list{c}")
else:
    print(len(a))



