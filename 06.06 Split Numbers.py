def isEven(num):
    return num % 2 == 0
def isOdd(num):
    return num % 2 != 0   
def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    else:
        return True

inputFile = open("06.06 Numbers.txt","r")
evenNumbersFile = open("06.06 Evennumbers.txt","w")
oddNumbersFile = open("06.06 Oddnumbers.txt","w")
primeNumbersFiles = open("06.06 Primenumbers.txt","w")

numCount = 0
oddCount = 0
evenCount = 0
primeCount = 0

for line in inputFile:
    line = int(line.strip())
    numCount = numCount + 1
    
    if isEven(line):
        evenNumbersFile.write(str(line) + "\n")
        evenCount = evenCount + 1   
    if isOdd(line):
        oddNumbersFile.write(str(line) + "\n")
        oddCount = oddCount + 1   
    if isPrime(line):
        primeNumbersFiles.write(str(line) + "\n")
        primeCount = primeCount + 1 

inputFile.close()        
evenNumbersFile.close()
oddNumbersFile.close()
primeNumbersFiles.close()

print(evenCount,"even numbers")
print(oddCount,"odd numbers")
print(primeCount,"prime numbers")
print(numCount,"number read")