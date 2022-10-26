file = open("Exam Two Names.txt", 'r') 

boynames = []
girlnames = []

for line in file.readlines():
    data = line.strip().split(',') 
    boynames.append(data[0].strip())
    girlnames.append(data[1].strip())


name = input("Enter a Name: ").strip()  



while name.lower() != "q": 
    for i in range(len(boynames)):
        if boynames[i] == name:
            print("Boy's Name {} - Rank {}".format(name, i + 1))
    for i in range(len(girlnames)):
        if girlnames[i] == name:
            print("Girl's Name {} - Rank {}".format(name, i + 1))
    else:
        print("Name not found")

    name = input("Enter a Name: ").strip()
