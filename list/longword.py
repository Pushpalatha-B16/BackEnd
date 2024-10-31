#Write a program to find the longest word in a given sentence
from re import*
a="python is a high level programming language"
word=split(" ",a)
maximum=word[0]
for i in word:
   if len(maximum)<len(i):
      maximum=i
print(f"longest word in sentence:{maximum}")
