numbers = [2,7,11,15]
target = 9
low = 0
high= len(numbers) - 1

while low < high:
    if numbers[low]+numbers[high] == target:
        print(low,high)
    elif numbers[low]+numbers[high] < target:
        low +=1
    else:
        high -=1
