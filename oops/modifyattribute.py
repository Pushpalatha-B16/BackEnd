"""7)Write a  Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified
values of the said attributes"""

class Student:
    def __init__(self,name,marks):
        self.student_name=name
        self. marks=marks
    def display(self):
        print(f"student name:{self.student_name}")
        print(f"student marks:{self.marks}")
print("original values")     
s=Student("anu",88)
s.display()      
print("Modified values")
s.student_name="Anu"
s.marks=98
s.display()
