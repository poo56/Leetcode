#Given two strings, str1 and str2, find the index of the extra character that is present in only one of the strings.
# string 1 = “pqr”
#string 2 = “psrq”

#Using Naive approach

def find_index_of_extra_character(s1, s2):
    if len(s1) > len(s2):
        longer_str = s1
        shorter_str = s2
    else:
        longer_str = s2
        shorter_str = s1

    # XOR all characters to find the extra character
    result = 0
    for char in longer_str:
        result ^= ord(char)

    for char in shorter_str:
        result ^= ord(char)

    # The result is the ASCII value of the extra character
    extra_char = chr(result) #converting ASCII to character

    # Find the index of the extra character in the longer string
    index = longer_str.index(extra_char)

    return index
# Example usage:
s1 = "cbda"
s2 = "abc"
index = find_index_of_extra_character(s1, s2)
print("Index of the extra character:",index)