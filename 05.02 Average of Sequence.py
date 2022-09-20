sum = 0
counter = 0
x = int(input ("Enter a Number (zero to quit): "))
while x != 0 :
    sum = sum + x
    counter = counter + 1
    x = int(input ("Enter a Number (zero to quit): "))
if counter == 0 :
    print("Sequence Length is 0")
else:
    print("Average: ", sum/counter)