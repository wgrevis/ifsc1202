x = int(input ("Enter a Number (zero to quit): "))
maximum = x
counter = maximum
while x != 0 :
    if x > maximum:
        maximum = x
    if x == x :
        times = counter + maximum
    x = int(input ("Enter a Number (zero to quit): "))
print("Maximum: ", maximum)
print("Number of Occurrences: ", times)