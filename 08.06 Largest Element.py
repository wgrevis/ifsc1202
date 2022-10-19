x = input("Enter Values Saparated by Spaces: ")

nums = x.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

largeindex = 0
largevalue = nums[0]

for i in range(1, len(nums)):
    if nums[i] > largevalue:
        largevalue = nums[i]
        largeindex = i

print("Largest Value:",(largevalue))
print("Index of Largest Value:", (largeindex))