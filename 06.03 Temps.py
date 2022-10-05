def FahrToCel(fahrenheit):
    return(float(fahrenheit) - 32) * 5 / 9
ftemp = open("06.03 FTemps.txt", "r")
ctemp = open("06.03 CTemps.txt", "w")
ctemp.write("")
f = ftemp.readline().strip()
records = 0
while f != "":
    c = FahrToCel(f) 
    c = round(c,1)
    ctemp = open("06.03 CTemps.txt", "a") 
    ctemp.write(str(c) + '\n')
    ctemp.close()
    f = ftemp.readline().strip()
    records = records + 1
print("{} records written".format(records))
