x = int(input("Enter a Number (zero to quit): "))
maximum = x
counter = 0
while x != 0 :
    x = int(input("Enter a Number (zero to quit): "))
    if x > maximum:
        maximum = x
    if x == x :
        counter = counter + 1 
    print("{} repeated {} number of times.".format(maximum, counter))