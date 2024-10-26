def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i +=1
        j -=1
    return True

def main():
    test_cases = ["madam","ABC"]
    for i in range(len(test_cases)):
        print(is_palindrome(test_cases[i]))

if __name__ == '__main__':
    main()
