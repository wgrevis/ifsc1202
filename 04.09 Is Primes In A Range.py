a = int(input ("Enter A: "))
b = int(input ("Enter B: "))
for i in range(2, a//2 + 1):
    if a % i == 0:
        print(i)
for i in range(2, b//2 + 1 ):
    if b % i == 0:
        print(i)