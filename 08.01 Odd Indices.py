x= input("Enter Values Separated by Spaces: ")
numbers=x.split()
for i in numbers[1::2]:
    print(i)