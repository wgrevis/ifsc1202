x = input("Enter Values Seperated by Spaces : ")
nums = x.split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

count = 1

for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[i] == nums[j]:
            break
        if i == j + 1:
            count = count + 1

print("Number of Distinct Elements:", count)