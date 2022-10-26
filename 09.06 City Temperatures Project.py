file = open("09.06 CityTemps.txt","r")
cityTempList = []

row = file.readline()

while row != "":
    data = row.strip().split()
    cityTempList.append(data)
    row = file.readline()

for i in range(0, len(cityTempList)):
    avg = 0
    for j in range(1, len(cityTempList[i])):
        cityTempList[i][j] = int(cityTempList[i][j])
        avg = avg + cityTempList[i][j]
    avg = avg / 7
    cityTempList[i].append(int(avg))

print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("City", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su", "Avg"))

for i in range(0, len(cityTempList)):
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(*cityTempList[i]))