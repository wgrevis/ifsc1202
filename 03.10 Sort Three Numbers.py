x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))
if x > z:
    x = x + z
    z = x - z
    x = x - z  
if x > y:
    x = x + y
    y = x - y
    x = x - y
if y > z:
    y = y + z
    z = y - z
    y = y - z
print (x, y, z)