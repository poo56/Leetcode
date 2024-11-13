def contains_duplicate():
    nums = [1,2,3,1]
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate())