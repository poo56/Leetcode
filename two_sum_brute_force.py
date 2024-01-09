
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    to_find_num = target - nums[i]
    for j in range(i+1, len(nums)):
        if to_find_num == nums[j]:
            print(i,j)