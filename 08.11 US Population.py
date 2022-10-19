fileUSPop = open("08.11 USPopulation.txt","r")

listUSPopulation = []

population = fileUSPop.readline()
while population != "":
    listUSPopulation.append(int(population.strip()) * 1000)
    population = fileUSPop.readline()

currentYear = 1950
avgChange = 0

minChange = 0
minChangeYear = 1950

maxChange = 0
maxChangeYear = 1950

print("{:<10} {:<10} {:<10} {:<10}".format("Year", "Population", "Change", "Percent Change"))

for i in range(0, len(listUSPopulation)):
    year = currentYear + i
    population = listUSPopulation[i]
    prevPopulation = listUSPopulation[i - 1]

    change = population - prevPopulation
    percentChange = (change / prevPopulation)

    if minChange > change:
        minChange = change
        minChangeYear = year
    if maxChange < change:
        maxChange = change
        maxChangeYear = year

    if i == 0:
        print("{:<10} {:<10} {:<10} {}".format(year, population, "N/A", "N/A"))
    else:
        avgChange = avgChange + change
        print("{:<10} {:<10} {:<10} {:.2%}".format(year, population, change, percentChange))

    if i == 1:
        minChange = change
        maxChange = change
        avgChange = change
print()
print("Average Change = {}".format(round(avgChange / len(listUSPopulation), 1)))
print("Minimum Change = {} ({})".format(minChange, minChangeYear))
print("Maximum Change = {} ({})".format(maxChange, maxChangeYear))