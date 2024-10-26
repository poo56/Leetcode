nums = [0,1,0,3,12]
pos = 0

for i in range(len(nums)):
    element = nums[i]
    if element != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        pos +=1
    print(nums)
