
"""8)Define a class Person with private attributes name and age. Provide public methods
to get and set the values of these attributes(Use getter and setter)"""

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__a=age
    def get(self):
        print("name:", self.__name)
        print("age:",self.__a)
    def set(self,n,age1):
        self.__name=n
        self.__a=age1
p=Person("anu",12)
p.get()
print("Modified data:")
p.set("Anu",14)
p.get()
