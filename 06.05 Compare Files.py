fileA= open("06.05 CompareFileA.txt","r") 
fileB= open("06.05 CompareFileB.txt","r")

different = 0
lineNumber = 0

lineA = fileA.readline()
lineB = fileB.readline()

while lineA != "":
    lineNumber = lineNumber + 1

    if lineA != lineB:
        print("Line:", lineNumber, "- File A: " + lineA)
        print("Line:", lineNumber, "- File B: " + lineB)
        
        different = different + 1

    lineA = fileA.readline()
    lineB = fileB.readline()

fileA.close()
fileB.close()

print(different,'differences')