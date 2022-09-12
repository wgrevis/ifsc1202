x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if x==y and y==z: 
    print("3")
if not x==y and not y==z:
     print("0")
if not x==y or not y==z and not z==x : 
    print("2")
