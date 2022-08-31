km = int(input("Enter Length of Race in Kilometers: "))
min = int(input("Enter Minutes: "))
s = int(input ("Enter Seconds: "))
miles = km / 1.61
hour = min / 60 + s / 3600
mph = miles / hour
print (mph)
