num = int(input("Enter a number: "))
num3 = num % 10
num2 = num // 10 % 10
num1 = num // 100 % 10
if num1 + 1 == num2 and num2 + 1 == num3: 
    print("YES")
else: 
    print("NO")