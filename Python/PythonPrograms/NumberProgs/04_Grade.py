# Find the grade of the student

s1=int(input("Enter subject1="))
s2=int(input("Enter subject2="))
s3=int(input("Enter subject3="))
s4=int(input("Enter subject4="))
s5=int(input("Enter subject5="))
s6=int(input("Enter subject6="))

avg=(s1+s2+s3+s4+s5+s6)/6

if(avg>90):
	print("Grade A")
elif(avg>80 and avg<90):
    print("Grade B")
elif (avg>70 and avg<80):
    print("Grade C")
elif (avg>60 and avg<70):
    print("First Division")
elif (avg>50 and avg<60):
    print("First Division")
else:
    print("Fail")