# How to calculate the number of vowels and consonants in a string
a=input()
vowels="aeiou"
vowels_c="AEIOU"
v_c=0
con=0
for i in a:
    if (i in vowels) or (i in vowels_c) :
        v_c+=1
    else:
        con+=1
print(f"Number of vowels in string:{v_c}")
print(f"Number of consonants in string:{con}")
        
