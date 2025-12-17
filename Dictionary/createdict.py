#create dictionary with information about a person(name,age and city)and print it
person={"person'sname":"anu","person's age":12,"person's city":"chennai"}
print(person)
#Add a new key-value pair for person's job and print updated dictionary
person["person's job"]="manager"
print(f"after adding job:{person}",end="\n")
#update person's age and print updated dictionary
person["person's age"]=22
print(f"after updated age:{person}")
#Remove the person's city from the dictionary and print the updated dictionary
del person["person's city"]
print(f"after remove person's city:{person}")
#Loop through the dictionary and print each key and value
for key,value in person.items():
    print(f"key:{key} value:{value}")
