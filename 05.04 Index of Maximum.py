x = int(input ("Enter a Number (zero to quit): "))
maximum = x
while x != 0 :
    if x > maximum:
        maximum = x
    index = maximum - maximum + 2
if x == 0:
    index = 0
    x = int(input ("Enter a Number (zero to quit): "))
print("Maximum: ", maximum)
print("Index of Maximum: ", index)