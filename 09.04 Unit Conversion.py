
fromValue = float(input("Enter From Value: "))
fromUnit = input("Enter From Unit (mm,cm,m,km,in,yd,mi): ")
toUnit = input("Enter To Unit (mm,cm,m,km,in,yd,mi): ")

fromUnit = fromUnit.lower()
toUnit = toUnit.lower()

file = open("09.04 Conversion.txt","r")
conversionList = []

row = file.readline()
conversionList.append(row.strip().split())
row = file.readline()
while row != "":
    data = row.strip().split()
    for i in range(1, len(data)):
        data[i] = float(data[i])
    conversionList.append(data)
    row = file.readline()

fromIndex = -1
toIndex = -1

for i in range(len(conversionList)):
    if conversionList[i][0] == fromUnit:
        fromIndex = i

for i in range(len(conversionList[0])):
    if conversionList[0][i] == toUnit:
        toIndex = i


if fromIndex == -1:
    print("FromUnit is not valid")
elif toIndex == -1:
    print("ToUnit is not valid")
else:
    toValue = round(fromValue * conversionList[fromIndex][toIndex], 7)
    print ("{} {} => {} {}".format(fromValue, fromUnit, toValue, toUnit))
