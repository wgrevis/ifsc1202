x = (input("Enter the string: "))
firsth = x.find("h")
lasth = x.rfind("h")
inside = x[firsth:lasth+1]
print(x.replace(inside, ""))