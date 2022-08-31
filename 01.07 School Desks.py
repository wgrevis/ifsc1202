a =input("Enter Classroom A: ")
b =input("Enter Classroom B: ")
c =input("Enter Classroom C: ")
y = 2
classafull = int(a) // y
classapartial = int(a) % y
classbfull = int(b) // y
classbpartial = int(b) % y
classcfull = int(c) // y
classcpartial = int(c) % y
print(classafull + classbfull + classcfull + classapartial + classbpartial + classcpartial)