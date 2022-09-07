x = int(input("Enter a 3 Digit Number: "))
sum = x//100 + x%10 + x%100//10
print ("Sum of Digits: {}".format(sum))