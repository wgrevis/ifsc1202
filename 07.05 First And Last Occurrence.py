x = input("Enter a string: ")
if x.count ("f") == 1:
    firstf = x.find("f")
    print(firstf)
if x.count ("f") >= 2:
    firstf = x.find("f")
    lastf = x.rfind("f")
    print(firstf, lastf)
if x.count ("f") == 0: 
    print(0)