class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for word in strs:
            keys = "".join(sorted(word))
            if keys in dict:
                dict[keys].append(word)
            else:
                dict[keys] = [word]

        return list(dict.values())
