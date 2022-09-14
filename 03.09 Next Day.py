m = int(input("Enter Month: "))
d = int(input("Enter Day: "))
if (m == 1 and d == 31) or (m == 2 and d == 28) or (m == 3 and d == 31) or (m == 4 and d == 30) or (m == 5 and d == 31) or (m == 6 and d == 30) or (m == 7 and d == 31) or (m == 8 and d == 31) or (m == 9 and d == 30) or (m == 10 and d == 31) or (m == 11 and d == 30) :
    m = m + 1
    d = 1
elif (m == 12 and d == 31) :
    m = 1
    d = 1
else :
    d = d + 1
print ("{}/{}".format(m , d))