x = int(input("Enter Number of Cards: "))
for i in range (1, x): 
    x1 = int(input("Enter Card: "))
    sum1 = x + x1
    sum2 = x1 + i + 2
    sum = sum2 - sum1
print("Missing Card: ", sum)
print(sum2)
print(sum1)