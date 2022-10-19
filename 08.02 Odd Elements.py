s = input("Enter Values Separated by Spaces: ")
lst = s.split()
for x in range(0, len(lst)):
    if int(lst[x]) % 2 == 1:
        print(lst[x])