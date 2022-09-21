a = int(input ("Enter A: "))
b = int(input ("Enter B: "))
v = (a , b)
for i in range(2, v//2 + 1):
    if v % i == 0:
        print("Number")