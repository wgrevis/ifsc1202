s = input("Enter Values Seperated by Spaces: ")

nums = s.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

minIndex = 0
maxIndex = 0

for i in range(0, len(nums)):
    if nums[i] < nums[minIndex]:
        minIndex = i
    if nums[i] > nums[maxIndex]:
        maxIndex = i

temp = nums[minIndex]
nums[minIndex] = nums[maxIndex]
nums[maxIndex] = temp

print("Swapped minimum and maximum: ", end="")

for i in range(0, len(nums)):
    print(nums[i], end=" ")

print()