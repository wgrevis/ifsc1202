x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if x==y and y==z: 
    print("3")
elif x==y or y==z or x==z :
    print("2")
else :
    print("0")
