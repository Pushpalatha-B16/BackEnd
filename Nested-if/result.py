"""
Write a program that determines if a student passes or fails based on their scores in three subjects. Use the following conditions:

If the average score is 50 or above, and the student has no score below 40 in any subject, they pass.

If the average score is 50 or above, but the student has at least one score below 40, they fail.

If the average score is below 50, they fail.

"""
sub1=int(input("sub1:"))
sub2=int(input("sub2:"))
sub3=int(input("sub3:"))
avg=(sub1+sub2+sub3)/3
if avg>=50:
    if sub1>=40 and sub2>=40 and sub3>=40:
        print("Pass")
    else:
         print("Fail")

else:
    print("Fail")
