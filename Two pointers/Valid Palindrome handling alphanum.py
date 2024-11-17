def valid_palindrome():
    s = "Was it a car or a cat I saw?"
    joint = ''.join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(joint) - 1
    while left <= right:
        if joint[left] == joint[right]:
            left +=1
            right -=1
        else:
            return False
    return True

print(valid_palindrome())