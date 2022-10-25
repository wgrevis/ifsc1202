fileNumbersList = open("09.02 NumbersList.txt","r")

def print_list(a):
    r = len(a)
    for i in range(0, r):
        c = len(a[i])
        for j in range(0, c):
            print(a[i][j], end=' ')
        print()

def swap_columns(a, i, j):
    r = len(a)
    for x in range(0, r):
        temp = a[x][i]
        a[x][i] = a[x][j]
        a[x][j] = temp


numbersList = []

row = fileNumbersList.readline()
while row != "":
    numbersList.append(row.strip().split())
    row = fileNumbersList.readline()

for i in range(0, len(row)):
    for j in range(0, len(row[i])):
        row[i][j] = int(row[i][j])

print_list(numbersList)

i, j = input("Enter the columns to swap: ").split()
i = int(i)
j = int(j)

swap_columns(numbersList, i, j)

print_list(numbersList)