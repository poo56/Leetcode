nums = [5]
n = len(nums)
output = []

# For each element in the array, compute the product of all other elements
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:  # Skip the element at index i
            product *= nums[j]
    output.append(product)

print(output)

