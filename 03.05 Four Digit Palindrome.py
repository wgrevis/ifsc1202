a = int(input("Enter a Number: "))
units = a % 10
a = a // 10
tens = a % 10 
a = a // 10
hundreds = a % 10
thousands = a // 10
if thousands == units and hundreds == tens :
    print("YES")
else :
    print ("NO")