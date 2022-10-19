s = input("Enter Values Separated by Spaces: ")
lst = []
for x in s.split(" "):
    lst.append(int(x))
i = 0
while i<len(lst):
    if(i+1<len(lst)):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    i = i + 2
print("Swapped Values: ",end="")
for x in lst:
    print(x,end=" ")