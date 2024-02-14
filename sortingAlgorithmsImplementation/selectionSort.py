arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4]

for i in range(len(arr)):
    min = i
    temp = arr[min]
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j

    arr[i]  = arr[min]
    arr[min] = temp



for i in range(len(arr)):
    print(arr[i])
