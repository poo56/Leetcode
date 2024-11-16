from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# solution 1
        #return sorted(s) == sorted(t) time complexity: O(n logn)
    #solution2
        #return Counter(s) == Counter(t) time complexity: O(n)
        #solution 3
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        if countS == countT:
            print(True)


