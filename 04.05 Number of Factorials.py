n = int(input("Enter Number: "))
factorial = 1
sum = 0 
for i in range(1, n + 1):
    factorial = factorial * i
    sum = sum + factorial
print("Sum of Factorials: ",sum)