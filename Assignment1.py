# This admission program  calculate the aggregate score and tell the students the faculty and department
# he or she is likely to be admitted to.

# To calculate grade of the students,
# Ask user to enter marks obtained in 5 subjects and store it in different variables.
# Now calculate the sum of all the marks and then use an else condition to calculate the average marks to find the grade
# according to the average marks obtained by student as shown in the program given below:


sub1 = float(input("Enter marks of the first subject: "))
sub2 = float(input("Enter marks of the second subject: "))
sub3 = float(input("Enter marks of the third subject: "))
sub4 = float(input("Enter marks of the fourth subject: "))
sub5 = float(input("Enter marks of the fifth subject: "))

# avg=(sub1+sub2+sub3+sub4+sub4)/5

total = sub1 + sub2 + sub3 + sub4 + sub4
avg = total / 5
print(avg)

# Criteria for admission score
if avg >= 80:
    print('Admission into faculty of medicine and law')
elif 75 <= avg <= 79:
    print("Admission into faculty of banking and finance, insurance and accountancy")
elif 71 <= avg <= 74:
    print("Admission into faculty of Pharmacy, physiology, pharmacology and nursing")
elif 61 <= avg <= 70:
    print("Admission into faculty of Computer science, psychology and statistics")
elif 55 <= avg <= 60:
    print("Admission into faculty of botany, zoology")
elif 50 <= avg <= 54:
    print("Admission into faculty of Agricultural science department")
else:
    print("No admission")
