
def findMin():

    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2

        # If middle element is greater than the high element, the minimum must be on the right
        if nums[mid] > nums[high]:
            low = mid + 1
        # Otherwise, the minimum is on the left including mid
        else:
            high = mid

    # When low == high, we've found the minimum element
    return nums[low]