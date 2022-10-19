s = input("Enter Values Separated by Spaces: ")
numbers = s.split()
for i in range(1, len(numbers)):
    prev = int(numbers[i - 1])
    curr = int(numbers[i])
    if curr > prev:
        print(curr)