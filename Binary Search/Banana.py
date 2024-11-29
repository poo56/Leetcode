'''

Approach 1 : Using Brute Force
def banana():
    piles = [25,10,23,4]
    h = 4


    for speed in range(1,max(piles)+1):
        totalTime = 0
        for pile in piles:

            totalTime += math.ceil(pile/speed)

        if totalTime <= h:
            return speed
    return max(piles)


print(banana())
'''

Approach 2 using Binary search(optmized)

def banana():
    piles = [25, 10, 23, 4]
    h = 4

    low = 1
    high = max(piles)
    res = 0
    r = 0

    while low <= high:
        mid = (low+high)//2

        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile/mid)

        if totalTime <= h:
            #If this is true then store the result of the number in res and still check to find the smallest element
            res = mid

            high = mid - 1
        else:
            low = mid + 1
    return res