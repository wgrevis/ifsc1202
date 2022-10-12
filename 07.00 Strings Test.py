course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
# \ is used to escape after (escape character)
# \'
# \""
# \n new line
first = "William"
last = "Revis"
full = f"{first} {last}"
#another way of replacing
full2 = f"{len(first)} {5+2}"
print(full)
print(full2)

# . functions
course3 = "python programming"
print(course3.upper())
print(course3.lower())
print(course3.title()) #cap first letter of every word
print(course3.strip())
print(course3.lstrip())
print(course3.rstrip())
print(course3.find("pro"))
print(course3.replace("p", "j"))
print("pro" in course3)
print("swift" not in course3)