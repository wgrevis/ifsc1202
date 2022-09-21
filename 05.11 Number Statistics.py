sum = 0
counter = 0
x = int(input ("Enter a Number (zero to quit): "))
maximum = (float(x))
minimum = (float(x))
while x != 0 :
    counter = counter + 1
    sum = sum + x
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
    x = float(input ("Enter a Number (zero to quit): "))
print("Count:   ", counter)
print("Sum:     ", sum)
print("Average: ", sum/counter)
print("Minimum: ", minimum)
print("Maximum: ", maximum)