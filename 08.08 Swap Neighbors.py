s = input("Enter Values Separated by Spaces: ")
nums = s.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

for i in range(0, len(nums), 2):
    if(i + 1 < len(nums)):
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp

print("Swapped Values: ", end="")

for i in range(0, len(nums)):
    print(nums[i], end=" ")

print()
