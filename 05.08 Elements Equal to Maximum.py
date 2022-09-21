x = int(input ("Enter a Number (zero to quit): "))
maximum = x
counter = 0
while x != 0 :
    if x > maximum:
        maximum = x
    if x == x :
        counter = counter + 1
    x = int(input ("Enter a Number (zero to quit): "))
print("Maximum: ", maximum)
print("Number of Occurrences: ", counter)