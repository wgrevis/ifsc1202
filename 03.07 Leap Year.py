x = int(input("Enter Year: "))
if ((x % 4==0) and (x % 100 != 0 )) or (x % 400==0) :
    print("LEAP YEAR")
else :
    print("COMMON YEAR")