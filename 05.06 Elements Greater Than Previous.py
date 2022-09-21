x = int(input ("Enter a Number (zero to quit): "))
counter = 0
while x != 0:
    if x > x - 1 : 
        counter = counter + 1
    x = int(input ("Enter a Number (zero to quit): "))
print("Number of Values Greater Than the Previous: ",counter)