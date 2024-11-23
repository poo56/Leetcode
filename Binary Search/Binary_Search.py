def search():
    nums = [0,2,3,4,5,6,7]
    target = 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + ((right - left)//2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


print(search())


