y = int(input ("Enter First Number (zero to quit): "))
z = int(input ("Enter Second Number (zero to quit): "))
maximum = y
maximum2 = z
while y != 0:
    if y > maximum:
        maximum = y
    y = int(input ("Enter a Number (zero to quit): "))
    if z > maximum2:
        maximum2 = z
    y = int(input ("Enter a Number (zero to quit): "))
print("First Maximum: ", maximum)
print("Second Maximum: ", maximum2)