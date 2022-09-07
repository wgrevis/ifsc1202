f = int(input("Enter First 2 Digit Number: "))
s = int(input("Enter Second 2 Digit Number: "))
tensdigit1 = (f % 100) // 10
tensdigit2 = (s % 100) // 10
unitsDigit1 = f % 10
unitsDigit2 = s % 10
print("Swapped Number: {}{}{}{}".format(tensdigit1,tensdigit2,unitsDigit1,unitsDigit2))