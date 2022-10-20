s = input("Enter Values Seperated by Spaces: ")

nums = s.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

print("Unique Elements: ", end="")

for i in range(0, len(nums)):
    isUnique = True
    for j in range(0, len(nums)):
        if nums[i] == nums[j] and i != j:
            isUnique = False
            break
    if isUnique:
        print(nums[i], end = " ")
print()