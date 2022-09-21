x = int(input("Enter a Number (zero to quit): "))
maximum = x
counter = 0
while x != 0 :
    if x > maximum:
        maximum = x
    if x == x :
        times = counter + 1 
print ("{} repeated {} times.".format(x, times))