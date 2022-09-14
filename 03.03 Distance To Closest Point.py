a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))
distance = 0
ab= abs(a - b)
ac= abs(a - c)
if ab < ac :
    print(ab)
else :
    print(ac)