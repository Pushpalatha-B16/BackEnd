"""
Write a program that calculates the final grade of a student based on their score and whether they completed extra credit assignments. Use the following conditions:

If the score is above 90 and extra credit is completed, the final grade is "A+".

If the score is above 90 and extra credit is not completed, the final grade is "A".

If the score is between 80 and 90 and extra credit is completed, the final grade is "B+".

If the score is between 80 and 90 and extra credit is not completed, the final grade is "B".

Repeat similar logic for grades "C", "D", and "F".
"""
score=int(input("Score"))
extra=input("status of extra credit:")
if score>60:
    if score>60 and score<70 and extra=="yes":
        print("D+")
    elif score>70 and score<80 and extra=="yes":
        print("C+")    
    elif score>70 and score<80 and extra=="no":
        print("C")
    elif score>80 and score<90 and extra=="yes":
     print("B+")
    elif score>80 and score<90 and extra=="no":
      print("B")
    elif score>90 and score<80 and extra=="yes":
       print("A+")
    else:
        print("A")
else:
    print("F")
