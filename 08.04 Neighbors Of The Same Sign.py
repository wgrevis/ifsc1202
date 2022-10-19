x = input("Enter Values Seprated by Spaces: ")

nums = x.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

for i in range(0, len(nums) - 1):
    if nums[i] > 0 and nums[i + 1] > 0:
        print(nums[i],nums[i + 1])
    elif nums[i] < 0 and nums[i + 1] < 0:
        print(nums[i],nums[i + 1])