nums = [4,5,6]
target = 10
res = []
seen = {}
for i, num in enumerate(nums):
    sum_check = target - num

    if sum_check in seen:
        res.append((seen[sum_check], i))
    seen[num] = i