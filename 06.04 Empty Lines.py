fileToRead= open("06.04 EmptyLinesInput.txt","r") 
fileToWrite= open("06.04 EmptyLinesOutput.txt","a")

readCount=0
writeCount=0

line = fileToRead.readline()

while line != "":
    readCount = readCount + 1

    if line.strip():
        fileToWrite.write(line)
        writeCount = writeCount + 1

    line = fileToRead.readline()

fileToRead.close()
fileToWrite.close()

print(readCount,"records read")
print(writeCount,"records written")