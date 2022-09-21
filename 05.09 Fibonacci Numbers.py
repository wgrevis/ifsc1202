n = int(input("Enter Fibonnaci Sequence Number: "))
a = 0
b = 1
sum = 0
count = 1
while(count <= n):
  count += 1
  a = b
  b = sum
  sum = a + b
print("Fibonacci Number : ", count)  