x = input("Enter a string: ")
half = (len(x) + 1) // 2
firsthalf = x[:half]
secondhalf = x[half:]
reverse = secondhalf + firsthalf
print(reverse)