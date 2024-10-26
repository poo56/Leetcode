
def three_sum(nums, target):
    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True

            elif triplet < target:
                low += 1

            else:
                high -= 1
    return False

def main():
    nums = [8, 2, 4, 9, 5]
    nums.sort()
    target = 17
    print(three_sum(nums, target))


if __name__ == '__main__':
    main()