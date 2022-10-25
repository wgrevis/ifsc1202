r, c = input("Enter the number of rows and columns: ").split()

r = int(r)
c = int(c)

maxV = []

for i in range(0, r):
    x = input("Enter a line of data: ").split()
    maxV.append(x)

maxRow = 0
maxCol = 0

for i in range(0, r):
    for j in range(0, c):
        maxV[i][j] = int(maxV[i][j])
        print(maxV[i][j], end=' ')

        if maxV[i][j] > maxV[maxRow][maxCol]:
            maxRow = i
            maxCol = j
    print()

print("The maximum value {} occurred in row {} column {}".format(maxV[maxRow][maxCol], maxRow, maxCol))