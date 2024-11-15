def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
        return res


def decode(s:str):
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res
print(encode(["poo","sre"]))
print(decode("3#poo"))