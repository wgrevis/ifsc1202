x = int(input("Enter Number of Cards: "))
sum1 = 0
for i in range (1, x): 
    x1 = int(input("Enter Card: "))
    sum1 = sum1 + i
    sum2 = x1 + i
    sum = sum2 - sum1
print("Missing Card: ", sum)