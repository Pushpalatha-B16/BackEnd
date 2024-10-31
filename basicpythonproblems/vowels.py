a="aeiou"
b="AEIOU"
user=input("Enter string:")
count=0
for i in user:
    if(i in a or i in b):
        count+=1
print(count)   
