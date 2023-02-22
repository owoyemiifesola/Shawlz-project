sname=input("Student Name :")
admNo=input("Admission Number :")
fname=input("Father's Name :")
mname=input("Mother's Name :")
gender=input("Gender :")
sclass=input("Class :")
eng=float(input("English Marks:"))
maths=float(input("Maths Marks:"))
govt=float(input("Government Marks:"))
lit=float(input("Literature Marks:"))
crs=float(input("C.R.S Marks:"))
econs=float(input("Economics Marks:"))

total=eng+maths+govt++lit+crs+econs
percent=(eng+maths+govt+lit+crs+econs)/6
grade =""
if percent>=80:
    grade ="A1 EXCELLENT"
elif  percent>=70:
    grade ="B2 VERY GOOD"
elif percent>=65:
    grade="B3 GOOD"
elif percent>=60:
    grade="C4 CREDIT"
elif percent>=55:
    grade ="C5 CREDIT"
elif percent>=50:
    grade ="C6 CREDIT"
elif percent>=40:
    grade ="D7 PASS"
else:
    grade ="F9 FAIL"

max=(100)
min=(40)
print("*******************************************")
print("CODEVERSE ACADEMY")
print("IN AFFILIATION WITH T-MAX NIGERIA")
print("----------------------------------------------------------")
print("Student Name:", sname, "\t", "\t", "Admin No.:", admNo)
print("Father's Name:", fname, "\t", "\t", "Gender:", gender)
print("Mothers Name:", mname, "\t", "\t", "Class:", sclass)
print("----------------------------------------------------------")
print("Subject", "\t", "Max", "\t", "Min", "\t", "Marks obt")
print("English", "\t", max, "\t", min, "\t", eng)
print("Maths", "\t", "\t", max, "\t", min, "\t", maths)
print("Government", "\t", max, "\t", min, "\t", govt)
print("Literature", "\t", max, "\t", min, "\t", lit)
print("C.R.S", "\t", "\t", max, "\t", min, "\t", crs)
print("Economics", "\t", max, "\t", min, "\t", econs)
print("-------------------------------------------------------------")
print("Total Marks:","\t","\t","\t",total)
print("Percentage:","\t","\t","\t",percent)
print("Grade:","\t","\t","\t","\t","\t",grade)
print("--------------------------------------------------------------")
print("Class Teacher's Remark")
print("\t\t\t\t\t\t\t\t","Principal's signature")


