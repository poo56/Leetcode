nums = [7,1,2,3,9]
max_area = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):

        max_area = max(max_area, min(nums[i],nums[j]) * (j-i))

print(max_area)
        
