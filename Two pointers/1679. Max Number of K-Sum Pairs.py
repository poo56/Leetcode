nums = [1,2,3,4]
nums.sort()
k = 5
left = 0
right = len(nums)-1
count = 0

while left < right:
    if nums[left]+nums[right] < k:
        left +=1
    elif nums[left]+nums[right] > k:
        right -=1
    else:
        left +=1
        right -=1
        count +=1
print(count)