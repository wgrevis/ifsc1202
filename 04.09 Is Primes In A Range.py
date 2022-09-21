a = int(input ("Enter A: "))
b = int(input ("Enter B: "))
for i in range(2, n//2 + 1):
    if n % i == 0:
        print("COMPOSITE")
        break
else:
    print("PRIME")