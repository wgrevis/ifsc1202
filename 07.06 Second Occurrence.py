x = input("Enter a string: ")
if x.count ("f") > 1:
    firstf = x.find("f")
    secondf = x.find("f", firstf + 1)
    print(secondf)
if x.count ("f") == 1:
    print("One f")
if x.count ("f") == 0: 
    print("Zero f")