def search():
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


print(search())

